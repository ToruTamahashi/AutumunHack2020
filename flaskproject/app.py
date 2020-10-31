import uuid

from flask import Flask
from flask import jsonify
from flask import make_response,request
from flask_cors import CORS
from datetime import datetime

from .model.models import TaskEntity
from .model.models import UserService
from .model.models import TaskService
from .develop.self_req import get_req
from .develop.self_req import post_req
from .develop.self_req import oauth_test
from .auto_tweet import TwAPI
from .auto_tweet import OAuthTwitter
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, origin=['localhost', 'hackwebapps.net', 'autumn.hackwebapps.net'], allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE'], supports_credentials=True)


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
    return jsonify(str(a))


@app.route('/read/tasks', methods=['GET'])
def read_user_tasks():
    """
     指定のuser_idをもつタスクをtaskテーブルから全件取得
    :return:json [{'id':1,'title':'***',...}, {'id':3,'title':'***',...},...]
    """
    #param = request.get_json(force = True)
    ts = TaskService()
    #task_list = ts.find(param['user_id'])
    task_list = ts.find(1)
    task_dict_list=[]
    for i, task in enumerate(task_list):
        print(i, task)
        task.deadline_at = translate_datetime(task.deadline_at)
        task_dict_list.append(task.task_entity_dict())
    return jsonify(task_dict_list)

@app.route('/create/task', methods=['POST'])
def create_task():
    """
    taskテーブルにタスクを追加する
    :param json ex) {'title':'***','tweet':*,'mail':'***@***.com','deadline_at':'2020/10/31/06:22:18'}
    :return:json ex) {'result':'success'} or {'result':'failure'}
    """
    param = request.get_json(force=True)
    te = TaskEntity()
    te.title = param['title']
    te.tweet = param['tweet']
    te.mail = param['mail']
    te.deadline_at = param['deadline_at']
    te.user_id = 1
    ts = TaskService()
    return jsonify(ts.create(te))

@app.route('/update/task', methods=['POST'])
def update_task():
    """
    taskテーブルのタスクを更新する
    :param json ex) {'id':1,'title':'***','tweet':*,'mail':'***@***.com','deadline_at':'2020/10/31/06:22:18'}
    :return:json ex) {'result':'success'} or {'result':'failure'}
    """
    param = request.get_json(force=True)
    task = TaskEntity()
    task.id = param['id']
    task.title = param['title']
    task.tweet = param['tweet']
    task.mail = param['mail']
    task.deadline_at = param['deadline_at']
    ts = TaskService()
    return jsonify(ts.update(task))

@app.route('/destroy/task', methods=['POST'])
def destroy_task():
    """
        taskテーブルのタスクを削除する
        :param json ex) {'id':1}
        :return:json ex) {'result':'success'} or {'result':'failure'}
        """
    param = request.get_json(force=True)
    ts = TaskService()
    return jsonify(ts.delete(param['id']))


@app.route('/req')
def self_request():
    res = post_req()
    res = get_req()
    res = oauth_test()
    return res.text

@app.route('/user_info', methods=['POST'])
def user_info():
    """
    ユーザ情報を取得します。（ユーザ名,twitter_id）
    :param　json ex) {'access_token_key':'*****','access_token_secret':'*****'}
    :return: json ex) {'name':'***','twitter_id':'****'}
    """
    access_token_dict = request.get_json(force=True)
    tw = TwAPI()
    user = tw.get_user_info(access_token_dict['access_token_key'],access_token_dict['access_token_secret'])
    user_info = {'name':user.name,'twitter_id':user.screen_name}
    return jsonify(user_info)



@app.route('/token_cookie', methods=['POST'])
def token_cookie():
    """
    認証後リダイレクト先のurlに付与されているパラメータを受け取りアクセストークン発行後cookieを設定する
    :param json
            ex)  {'oauth_token':'*****','oauth_verifier':'*****'}
    :return:json
            ex)  {'result':'success'}
    """
    oauth_dict = request.get_json(force=True)
    print(oauth_dict['oauth_token'])
    print(oauth_dict['oauth_verifier'])
    ot = OAuthTwitter()
    twitter_id = ot.get_access_token(oauth_dict)
    # セッションidを登録する
    us = UserService()
    user = us.find(twitter_id)
    user.session_id = str(uuid.uuid4())
    us.update(user)
    # cookieを設定する
    data = request.cookies.get('data')

    response = make_response(jsonify({'result':'success'}))
    max_age = 60 * 10  # 有効期限を設定
    expires = int(datetime.now().timestamp()) + max_age  # 有効期限の日時
    response.set_cookie('data', value=user.session_id, max_age=max_age,
                        expires=expires,samesite=None,)  # Cookieに値をセット

    return response


@app.route('/post_tweet', methods=['POST'])
def get_task():
    #twitter.post_tweet()
    return "b"

@app.route('/session', methods=['GET'])
def check_cookie():
    """
    cookieがあればtopページ、なければ認証ページのurlを返す
    :return:
    """
    data = request.cookies.get('data')
    redirect_url = None
    response = None
    if data is None:
        redirect_url = get_oauth_url()
        response = make_response(jsonify({'cookie':'none','url': redirect_url}))
    else:
        us = UserService()
        user = us.findBySessionID(data)
        if user is None:
            # 該当のセッションIDがなければ認証画面へ
            redirect_url = get_oauth_url()
            response = make_response(
                jsonify({'cookie': 'none', 'url': redirect_url}))
        else:
            # cookieがあれば有効期限を更新
            response = make_response(jsonify({'cookie':'exist'}))
            max_age = 60 * 10  # 有効期限を設定
            expires = int(datetime.now().timestamp()) + max_age  # 有効期限の日時
            response.set_cookie('data', value=data, max_age=max_age,expires=expires)  # Cookieに値をセット
    return response

def translate_datetime(value):
    return value.strftime('%Y/%m/%d/%H:%M:%S')

def get_oauth_url():
    """
    Twitter認証画面にリダイレクトさせるurlを返します
    :return: json
            ex) {'url','https://****'}
    """
    ot = OAuthTwitter()
    oauth_url = ot.get_redirect_url()
    print(oauth_url)
    #redirect_url = twitter.get_redirect_url()
    return oauth_url



def main():
    app.debug = True
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()