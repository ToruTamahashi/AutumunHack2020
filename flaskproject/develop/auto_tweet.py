import tweepy
import urllib

class TwitterAPI(object):
    def __init__(self):
        self.CONSUMER_KEY = "4KdK0UdVS9WvmvNsl17mWbyt4"
        self.CONSUMER_SECRET = "aIyPNAtCmqblwFlWhNjPbswXM7WVzig2AZcp8AtiNvkompbErY"
        self.Access_Token=""
        self.Access_Token_Secret=""
        # Twitterオブジェクトの生成
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.api = None

    def post_tweet(self):
        self.api.update_status("Pythonから投稿!")

    def get_user_info(self):
        user = self.api.me()
        print(user.screen_name)
        return user.screen_name

    def get_oauth_token(url:str)->str:
        querys = urllib.parse.urlparse(url).query
        querys_dict = urllib.parse.parse_qs(querys)
        return querys_dict["oauth_token"][0]

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
        oauth_token = self.get_oauth_token(redirect_url)
        print("oauth_token:", oauth_token)
        auth.request_token['oauth_token'] = oauth_token

    def post_verifier(self,oauth_verifier):
        """
        oauth_verifierパラメータを受け取ってアクセストークンを発行
        :param oauth_verifier:
        :return:
        """
        verifier = oauth_verifier
        self.auth.request_token['oauth_token_secret'] = verifier

        try:
            self.auth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error! Failed to get access token.')

        print("access token key:", self.auth.access_token)
        print("access token secret:", self.auth.access_token_secret)
        self.Access_Token = self.auth.access_token
        self.Access_Token_Secret = self.auth.access_token_secret

        self.auth.set_access_token(self.Access_Token, self.Access_Token_Secret)
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.api = tweepy.API(self.auth)

        with open("auth_info.text", mode="w") as file:
            text = "key:{}\nsecret:{}".format(self.auth.access_token,
                                              self.auth.access_token_secret)
            file.write(text)

        print("DONE")
        return





# 好きな言葉をツイート
#api.update_status("Pythonから投稿!")

