# coding:utf-8
import tweepy 

consumer_key = consumer_key
consumer_secret = consumer_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#自分のキー

access_token_key=''
access_token_secret=''
auth.set_access_token(access_token_key, access_token_secret)


# 以下は、アクセストークンをもらいにいく場合のコード。
# まず、認証コードを貰いに行くアドレスを取得する
redirect_url = auth.get_authorization_url()

# アドレスを表示し、ブラウザでアクセスして認証用コードを取得してくる。
print (redirect_url)

# ブラウザから取得してきた認証用コードを対話モードで入力する。
# strip()はコピペの際に末尾に改行コードとかスペースが入ったのを消すため。
verifier = input('Type the verification code: ').strip()
auth.get_access_token(verifier)

api = tweepy.API(auth)

# api.update_status(status='test2')

"""
user = api.get_user(screen_name="taka13twtr")
print (user.description)
"""

word = 'プログラミング'
set_count = 5
results = api.search(q=word, count=set_count)

"""
for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    user = result.user.name
    print("ユーザー名："+user)
    tweet = result.text
    print("ユーザーのコメント："+tweet)
"""
