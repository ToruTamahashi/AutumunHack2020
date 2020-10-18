from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from .model.models import UserEntity
from .model.models import TaskEntity
from .model.models import UserService
from .model.models import TaskService
from .develop.self_req import get_req
from .develop.self_req import post_req
from .develop.auto_tweet import TwitterAPI
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, origin=['localhost','hackwebapps.net','autumn.hackwebapps.net'],allow_headers=['Content-Type','Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE'])
twitter = TwitterAPI()

@app.route('/')
def hello_world():
    return 'helloworld!!!'


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

@app.route('/req')
def self_request():
    res = post_req()
    #res = get_req()
    return res.text

@app.route('/login', methods=['GET'])
def login():
    """
    Twitter認証画面にリダイレクトさせるurlを返します
    :return: String
    """
    redirect_url = twitter.get_redirect_url()
    return redirect_url

@app.route('/get_task', methods=['POST'])
def get_task():
    """
    oauth_verifierを受け取ってユーザ認証完了したらタスク一覧を返す
    :return:json
    """
    json_dict = request.get_json(force=True)
    print(json_dict['oauth_verifier'])
    #twitter.post_verifier(json_dict['oauth_verifier'])
    #twitter.post_tweet()
    return "a"

def main():
    app.debug = True
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()