import tweepy
import urllib
from ..model.models import UserEntity
from ..model.models import UserService

class TwAPI(object):

    def post_tweet(self):

        self.api.update_status("Pythonから投稿!")
        return "done"

    def get_user_info(self,AT,AS):
        CK = "4KdK0UdVS9WvmvNsl17mWbyt4"
        CS = "aIyPNAtCmqblwFlWhNjPbswXM7WVzig2AZcp8AtiNvkompbErY"

        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(CK, CS)
        auth.set_access_token(AT, AS)
        api = tweepy.API(auth)
        # ユーザ情報の取得
        user = api.me()
        print(user.screen_name)
        return user

    def regist_user_info(self,AT,AS):
        CK = "4KdK0UdVS9WvmvNsl17mWbyt4"
        CS = "aIyPNAtCmqblwFlWhNjPbswXM7WVzig2AZcp8AtiNvkompbErY"

        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(CK, CS)
        auth.set_access_token(AT, AS)
        api = tweepy.API(auth)
        # ユーザ情報の取得
        user = api.me()
        name = user.name
        twitter_id = user.screen_name
        us = UserService()
        user = us.find(twitter_id)
        # ユーザ情報が存在しなければ登録
        if (user == None):
            # UserEntityクラスをdictionaryに変換
            #user_dict = user.user_entity_dict()
            ue = UserEntity()
            ue.name = name
            ue.twitter_id = twitter_id
            us.create(ue)
        return "ok"


    

class OAuthTwitter(object):
    """docstring for OAuthTwitter"""
    def __init__(self):
        self.CONSUMER_KEY = "4KdK0UdVS9WvmvNsl17mWbyt4"
        self.CONSUMER_SECRET = "aIyPNAtCmqblwFlWhNjPbswXM7WVzig2AZcp8AtiNvkompbErY"
        self.Access_Token=None
        self.Access_Token_Secret=None
        # Twitterオブジェクトの生成
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)

    # def get_oauth_token(url:str)->str:
    #     querys = urllib.parse.urlparse(url).query
    #     querys_dict = urllib.parse.parse_qs(querys)
    #     return querys_dict["oauth_token"][0]

    def get_redirect_url(self):
        """
        ツイッター連携ページのurlを返します
        :return: string
        """
        try:
            # 認証画面にリダイレクトさせるurlを取得
            redirect_url = self.auth.get_authorization_url()
            print("Redirect URL:", redirect_url)
            return redirect_url
        except tweepy.TweepError:
            print("Error! Failed to get request token.")
            return "error"

            # リダイレクトurlに付与されているリクエストトークンを取得
        # oauth_token = self.get_oauth_token(redirect_url)
        # print("oauth_token:", oauth_token)
        # self.auth.request_token['oauth_token'] = oauth_token
        return "Finish"

    def get_access_token(self,oauth_dict):
        """
        oauth_token,oauth_verifierパラメータを受け取ってアクセストークンを発行
        :param oauth_verifier:
        :return:
        """
        self.auth.request_token['oauth_token'] = oauth_dict['oauth_token']
        self.auth.request_token['oauth_token_secret'] = oauth_dict['oauth_verifier']

        try:
            self.auth.get_access_token(oauth_dict['oauth_verifier'])
        except tweepy.TweepError:
            print('error')

        print("access token key:", self.auth.access_token)
        print("access token secret:", self.auth.access_token_secret)
        self.Access_Token = self.auth.access_token
        self.Access_Token_Secret = self.auth.access_token_secret

        # self.auth.set_access_token(self.Access_Token, self.Access_Token_Secret)
        # self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        # self.api = tweepy.API(self.auth)

        # ユーザ情報の登録
        tw = TwAPI()
        tw.regist_user_info(self.Access_Token,self.Access_Token_Secret)

        print("DONE")
        access_token = {"access_token_key":self.Access_Token, "access_token_secret":self.Access_Token_Secret}
        return access_token
        




# 好きな言葉をツイート
#api.update_status("Pythonから投稿!")

