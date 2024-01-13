import paho.mqtt.client as mqtt
from ecdsa import SigningKey, VerifyingKey
import importlib
import json
import time

# Configuration du broker MQTT
broker_address = "localhost"
broker_port = 1883
data_file = "data.txt"

#connection client mqtt 
client = mqtt.Client()
client.connect(broker_address, broker_port)
client.subscribe("request")

#Collecter les donner des esclaves et le rtourner sous forme de tableau 
def CollecteDataTask():
   donnees_esclaves = []
   taches = [
        "esclave_temp",
        "esclave_humidite",
        "esclave_co2",
        "esclave_ph"
    ]

   for tache in taches:
        module = importlib.import_module(tache)
        donnees_esclave = module.collecter_donnees()
        donnees_esclaves.append(donnees_esclave)
   return donnees_esclaves

def cryptingData(donnees):
    

    return

#transformer les donnees sous forme d'un fichier json et les communiquer au cloud avec le protocole MQTT
def on_message(client, userdata, message):
    if message.payload.decode() == "GET_DATA3":
        donnees = CollecteDataTask()
        donnees = json.dumps(donnees)
        payload = donnees
        client.publish("response2", payload)
        print("Les donneés sont publier ")
def destroyApp():
     client.disconnect()


if __name__ == "__main__":
    try: 
            client.on_message = on_message
            client.loop_forever()
           
    except:
        print("une Exeption arrête la publication des données...")   
        destroyApp()     
