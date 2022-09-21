import tweepy
from config import CONFIG

class Tweet:
    def __init__(self) -> None:
        # Twitter API
        API_KEY = CONFIG["CONSUMER_KEY"]
        API_SECRET = CONFIG["CONSUMER_SECRET"]
        ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
        ACCESS_TOKEN_SECRET = CONFIG["ACCESS_SECRET"]
        BEARER_TOKEN = CONFIG["BEARER_TOKEN"]

        # TwitterAPIの認証
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)
        print("Class Tweet Generated")
    def Tweet(self, TweetText):
        # 凍結避け、及びリプライにならないようにエスケープ
        self.api.update_status(TweetText.replace('殺', '.').replace('@', '@.'))
