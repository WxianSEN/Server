import requests
import json
from gevent import monkey;

monkey.patch_socket()
import gevent, time
from urllib.parse import urlencode

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
Header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}
URL = 'https://tool.zhuct.top/music/'

data = {
    'input': '阴天',
    'filter': 'name',
    'type': 'qq',
    'page': 1,
}


def get_info(type):
    start = time.time()
    print('开始运行了', type)
    data['type'] = type
    print(json.loads(requests.post(URL, urlencode(data), headers=Header).text))
    print(type, time.time() - start)


# response = requests.post(URL, urlencode(data), headers=Header).text
# print(json.loads(response))

# # 协程
# def get_success():
#     r = ''
#     while True:
#         n = yield r
#         if(len(n)>4):
#             musicList = n.data[0]
#
#
# def consumer():
#     # b.send(None)
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         data['type'] = n
#         response = json.loads(requests.post(URL, urlencode(data), headers=Header).text)
#         print('%s解析结果' % Type[n],response)
#     # b.close()
#
#
# def produce(c):
#     c.send(None)
#     Type_dict = [i for i in Type]
#     n = 0
#     while n < len(Type):
#         start = time.time()
#         curtype = Type_dict[n]
#         n = n + 1
#         r = c.send(curtype)
#         print(curtype, time.time()-start)
#     c.close()


# produce(consumer())

def request_web(url):
    start = time.time()
    print(len(requests.get(url).text), time.time()-start)

allstrat = time.time()
gevent.joinall([
    gevent.spawn(request_web, 'http://www.baidu.com'),
    gevent.spawn(request_web, 'http://www.360.com'),
    gevent.spawn(request_web, 'http://www.sougou.com'),
    gevent.spawn(request_web, 'http://www.xiaomi.com'),
    gevent.spawn(request_web, 'http://www.douyu.com'),
    gevent.spawn(request_web, 'http://www.huya.com'),
])
print('总时间', time.time()-allstrat)