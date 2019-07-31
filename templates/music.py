# 单线程版本

import time
import threading
import queue

# 用来存放筛选完音乐的列表
# curmusiclist = []
# 队列
queue = queue.Queue()
Type = {
    'qq': 'QQ',
    'netease': '网易云',
    'kugou': '酷狗',
    'kuwo': '酷我',
    'xiami': '虾米',
    'baidu': '百度',
    '1ting': '一听',
    'migu': '咪咕',
    'qingting': '蜻蜓',
    'ximalaya': '喜马拉雅',
    '5singyc': '51原唱',
    '5singfc': '51翻唱',
}


class Worker(threading.Thread):
    def __init__(self, name, queue, musicname):
        threading.Thread.__init__(self)
        self.queue = queue
        self.data = {
            'input': musicname,
            'filter': 'name',
            'type': 'qq',
            'page': 1,
        }
        self.name = name
        self.start()
        # 执行run()

    def isadd(self, info):
        if (info['code'] == 200):
            # curmusiclist.extend([info['data'][0], info['data'][1]])
            curmusiclist.append(
                {'src': info['data'][0]['url'],
                 'title': info['data'][0]['title'],
                 'cover': info['data'][0]['pic'],
                 'artist': info['data'][0]['author'],
                 'type': Type[info['data'][0]['type']],
                 })
            curmusiclist.append(
                {'src': info['data'][1]['url'],
                 'title': info['data'][1]['title'],
                 'cover': info['data'][1]['pic'],
                 'artist': info['data'][1]['author'],
                 'type': Type[info['data'][1]['type']],
                 })

    def get_info(self, data):
        import json
        import requests
        from urllib.parse import urlencode
        Header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
        }
        URL = 'https://tool.zhuct.top/music/'
        response = json.loads(requests.post(URL, urlencode(data), headers=Header, timeout=15).text)
        print(response)
        return response

    def run(self):
        # 循环，保证接着跑下一个任务
        while True:
            # 队列为空则退出线程
            if self.queue.empty():
                break
            # 获取一个队列数据
            foo = self.queue.get()
            # 延时1S模拟你要做的事情
            try:
                self.data['type'] = foo
                info = self.get_info(self.data)
                self.isadd(info)
                # 打印
                print(self.getName() + " 已解析 " + Type[foo])
            except:
                print('解析超时', foo)
            # 任务完成
            self.queue.task_done()


def run(a):
    global curmusiclist
    curmusiclist = []
    # 把所有解析加入个任务队列
    for i in Type:
        queue.put(i)
    # 开10个线程
    for i in range(len(Type)):
        threadName = 'Thread' + str(i)
        Worker(threadName, queue, a)
    # 所有线程执行完毕后关闭
    queue.join()
    print(curmusiclist)
    return curmusiclist
