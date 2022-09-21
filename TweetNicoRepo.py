
import json
import requests

from TweetCore import Tweet

# UserID : https://www.nicovideo.jp/user/xxxxxx/
UserID = 45489560




if __name__ == "__main__":

    TweetClient = Tweet()


    try:
        # 取得先URLにアクセス
        # 対象を抽出
        headers = {"content-type": "application/json"}
        APIreq = requests.get("https://public.api.nicovideo.jp/v1/timelines/nicorepo/last-6-months/users/"+UserID+"/pc/entries.json", headers=headers)
        APIjson = APIreq.json()
        ItemDescription = APIjson["data"][0]["title"]
        TweetHeader = (
            "いいね→" if "いいね" in ItemDescription 
            else "マイリス→" if "マイリスト" in ItemDescription 
            else "ニコニ広告→" if "ニコニ広告" in ItemDescription
            else "【動画投稿】 "if "動画を投稿しました"in ItemDescription
            else ItemDescription)
        ItemHref = APIjson["data"][0]["object"]["url"]
        ItemTitle = APIjson["data"][0]["object"]["name"]
        SmNumber = ItemHref.split("/")[-1]

        with open("TweetNicoRepo.latest","r") as f:
            if f.readline() != SmNumber:
                # 投稿者情報の取得
                r = requests.get("https://ext.nicovideo.jp/api/getthumbinfo/"+SmNumber)
                UpLoader = r.text.split("<user_nickname>")[1].split("</user_nickname>")[0]

                # Tweet文面の作成
                ItemTitle = ItemTitle if len(ItemTitle + SmNumber + UpLoader + " by") < 100 else ItemTitle[:(100 - len(ItemTitle + SmNumber + UpLoader + " by"))]+"..."
                TweetText = TweetHeader + ItemTitle + "\nby " + UpLoader +" " + ItemHref + " #" + SmNumber

                # Tweet送信
                print(TweetText)
                TweetClient.Tweet(TweetText)

        with open("TweetNicoRepo.latest","w") as f:
            f.write(SmNumber)
        
    finally:
        # プラウザを閉じる
        print("closed.")

