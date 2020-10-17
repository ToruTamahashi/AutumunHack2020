from flask import Flask
from flask import request
from flask import jsonify


from .model.models import UserEntity
from .model.models import TaskEntity
from .model.models import UserService
from .model.models import TaskService
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def hello_world():
    return 'helloworld!!!'


@app.route('/get', methods=['GET'])
def get_request():
    """
    受け取ったパラメータをそのまま返します
    :return:String
    """
    contents = request.args.get('value', '')
    return contents


@app.route('/post', methods=['POST'])
def show_post():
    """
    受け取ったパラメータをそのまま返します。
    :return:String
    """
    #a = request.values
    #print(a['username'])
    return str(request.values)

@app.route('/json')
def show_json():
    """
    Taskテーブルからデータをすべて取って返す
    :return json
    """
    ts = TaskService()
    a = ts.find_all()
    print(a[0]["id"])
    #a_dict = {key: value for key, value in a.__dict__.items()}
    return jsonify(str(a))

@app.route('/task/<id>')
def id_world(id):
    ts = TaskService()
    a = ts.find(id)
    # print(a[0])
    return jsonify(str(a))
    # return jsonify(str(a))

def main():
    app.debug = True
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()