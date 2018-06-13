import tweepy
import mysql.connector
import threading
import smtplib
from email.message import EmailMessage
import time

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
query = "Select id,text from tweet"
cursor.execute(query)
for t in cursor:
    tweets.append((t[0],t[1]))

# valores usados para enviar correo
FROM = 'empalidandoconrojo@gmail.com'
TO = 'rojo@tec.ac.cr' #rojo@tec.ac.cr
msg = 'Se han publicado los siguientes tweets: \n {} \n PD: que examen más rudo'
content = ""

def retrieveData():
    global content
    global msg
    while True:
        # Buscar tweets
        public_tweets = api.search('#intentadoSalvarElSemestreConRojo')
        # insertar tweets
        for tweet in public_tweets:
            id = tweet._json["id_str"]
            date = tweet._json["created_at"]
            text = tweet._json["text"]
            user = tweet._json["user"]["screen_name"]
            add_tweet = "INSERT INTO tweet (date, text, user, id) VALUES ('{}','{}','{}','{}')".format(date,text,user,id)
            try:
                cursor.execute(add_tweet)
                cnx.commit()
            except:
                continue
            tweets.append((id, text))
            if len(tweets)%10 == 0:
                print("Llegó a 10 tweets nuevos, enviar correo")
                for i in range(len(tweets)-10,len(tweets)):
                    content += str(i+1)+") "+tweets[i][1] + "\n"
                #Envia correo
                emsg = EmailMessage()
                emsg.set_content('lorem ipsum dolor amet')
                emsg['Subject'] = 'Ola ke ase, empalidando o ke ase'
                emsg['From'] = FROM
                emsg['To'] = TO

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("empalidandoconrojo@gmail.com", "#intentadoSalvarElSemestreConRojo")

                msg = msg.format(content)
                print(msg)

                server.sendmail(emsg['From'], emsg['To'], msg.encode())
                server.quit()

        time.sleep(60*5) #cada 5 minutos se repite el proceso


t = threading.Thread(target=retrieveData)
t.start()

#Cierra la conexión
# cursor.close()
# cnx.close()
