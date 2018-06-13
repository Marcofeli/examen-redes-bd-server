import tweepy
import mysql.connector
import threading

# Autentificacion
consumer_key = 'Vwx4h6GxWXva3SNnndSlETE17'
consumer_secret = 'G8NGqLTnlCMb37jSd8pRpNBfslutq2RaImtoh83abuKl066DrJ'

access_token = '1006632843907420160-e06w55i0ZU6oKLc5IkPy69vyuttqIB'
access_token_secret = 'vUwIpbKHsEXzOq8GCiIJEug8A1CQ9cCLImmmSc1hfSrtj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='examenredes')
cursor = cnx.cursor()

# Lista de tweets
tweets = list()
query = "Select id from tweet"
cursor.execute(query)
for (id) in cursor:
    tweets.append(id[0])


def retrieveData():
    while True:
        # Buscar tweets
        public_tweets = api.search('#intentadoSalvarElSemestreConRojo')
        # insertar tweets
        for tweet in public_tweets:
            id = tweet.id_str
            if id in tweets:
                continue
            date = tweet.created_at
            text = tweet.text
            add_tweet = "INSERT INTO tweet (date, text, user, id) VALUES ('{}','{}','{}','{}')".format(date,text,tweet.user._json["screen_name"],tweet.id_str)
            cursor.execute(add_tweet)
            cnx.commit()
            tweets.append(id)
            if len(tweets)%10 == 0:
                print(len(tweets))
                print("Llegó a 10 tweets nuevos, enviar correo")

def main():
    t = threading.Thread(target=retrieveData)
    t.start()

#Cierra la conexión
# cursor.close()
# cnx.close()

main()