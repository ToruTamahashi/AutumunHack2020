import json
from flask import Flask
from flask import request
from flask import jsonify

from .model.models import UserEntity
from .model.models import TaskEntity
from .model.models import UserService
from .model.models import TaskService
from .develop.self_req import get_req
from .develop.self_req import post_req
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def hello_world():
    return 'helloworld-2'


@app.route('/get', methods=['GET'])
def get_request():
    """
    受け取ったパラメータをそのまま返します
    :return:String
    """
    contents = request.args.get('value')
    return contents


@app.route('/post', methods=['POST'])
def show_post():
    """
    受け取ったパラメータをそのまま返します。
    :return:String
    """
    json_dict = request.get_json(force = True)
    print(json_dict[0]['name'])
    return jsonify(json_dict)

@app.route('/json')
def show_json():
    """
    Userテーブルからデータをすべて取って返す
    :return json
    """
    us = UserService()
    array = us.find_all()
    a = array[0]
    print(a.name)
    #a_dict = {key: value for key, value in a.__dict__.items()}
    a_dict = a.__dict__
    return str(a_dict)

@app.route('/req')
def self_request():
    res = post_req()
    #res = get_req()
    return res.text

def main():
    app.debug = True
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()