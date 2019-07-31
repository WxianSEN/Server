from flask import Flask, jsonify

from flask import abort

from flask import make_response

from flask import request

from flask_cors import cross_origin

app = Flask(__name__)

jobs = [
    {
        'success': True,
    }
]


@app.route('/api/Music', methods=['POST'])
@cross_origin()
def get_music():
    print(request.form['name'])
    import music
    if len(request.form['name']):
        response = music.run(request.form['name'])
        return jsonify({'success': True, 'Info': response})
    else:
        return jsonify({'success': False})


@app.route('/api/Info', methods=['POST'])
@cross_origin()
def get_tasks():
    if request.form['username'] == 'admin' and request.form['password'] == 'wuqiang':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@cross_origin()
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, jobs)

    # print (list(task))

    task = list(task)

    if len(task) == 0:
        abort(404)

    return jsonify({'task': task})


if __name__ == '__main__':
    app.debug(True)
    app.run()
