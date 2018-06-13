import tweepy
import mysql.connector

# Autentificacion
consumer_key = 'Vwx4h6GxWXva3SNnndSlETE17'
consumer_secret = 'G8NGqLTnlCMb37jSd8pRpNBfslutq2RaImtoh83abuKl066DrJ'

access_token = '1006632843907420160-e06w55i0ZU6oKLc5IkPy69vyuttqIB'
access_token_secret = 'vUwIpbKHsEXzOq8GCiIJEug8A1CQ9cCLImmmSc1hfSrtj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Buscar tweets
public_tweets = api.search('#intentadoSalvarElSemestreConRojo')

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='examenredes')
cursor = cnx.cursor()

for tweet in public_tweets:
    date = tweet.created_at
    text = tweet.text
    add_tweet = "INSERT INTO tweet (date, text, user, id) VALUES ('{}','{}','{}','{}')".format(date,text,tweet.user._json["screen_name"],tweet.id)
    print(add_tweet)
    cursor.execute(add_tweet)
    cnx.commit()
    print(tweet.user._json["screen_name"])

cursor.close()
cnx.close()