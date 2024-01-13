import time
import paho.mqtt.client as mqtt
import json
import joblib
import sklearn
import pandas as pd


# Configuration du broker MQTT
broker_address = "localhost"
broker_port = 1883
excel_file = "data.txt"
Model = joblib.load('modele_rf.pkl')


message_finish = True
client = mqtt.Client()
client.connect(broker_address, broker_port)
client.subscribe("response")
client.subscribe("response1")
client.subscribe("response2")
client.subscribe("response3")

def on_message(client, userdata, message):
        global message_finish, Type 
        Type = "."
        msg = message.topic
        if msg == "response":
            if not message_finish:
                return
            else:
                message_finish = False
                donnees = str(message.payload.decode("utf-8","ignore"))
                donnees = json.loads(donnees)
                
                if donnees[0] == None:
                    X_test = [donnees[2],donnees[1],donnees[3]]
                    X_test = pd.DataFrame([X_test],columns=['co','humidity','light'])
                    
                    temp = Model.predict(X_test)
                    donnees[0] = round(temp[0],2)
                    Type = "avec la prédiction"
                    
               # print("donnee apres",donnees,"\n")
                sauvegarder_donnees_excel(donnees,"data_noeud1.txt")  
                print("les données de noeud1 sont sauvegarder" + Type)
                message_finish = True
        elif msg == "response1":
            if not message_finish:
                return
            else:
                message_finish = False
                donnees = str(message.payload.decode("utf-8","ignore"))
                donnees = json.loads(donnees)
                sauvegarder_donnees_excel(donnees,"data_noeud2.txt")
                #client.publish("noeud1",donnees)
                print("les données de noeud2 sont sauvegarder.")
                message_finish = True
        elif msg == "response2":
            if not message_finish:
                return
            else:
                message_finish = False
                donnees = str(message.payload.decode("utf-8","ignore"))
                donnees = json.loads(donnees)
                sauvegarder_donnees_excel(donnees,"data_noeud3.txt")
                print("les données de noeud3 sont sauvegarder.")
                message_finish = True
        elif msg == "response3":
            if not message_finish:
                return
            else:
                message_finish = False
                donnees = str(message.payload.decode("utf-8","ignore"))
                donnees = json.loads(donnees)
                sauvegarder_donnees_excel(donnees,"data_noeud4.txt")
                print("les données de noeud4 sont sauvegarder.")
                message_finish = True

def sauvegarder_donnees_excel(donnees,dataset):
    donnees = list(donnees)
    with open(dataset, 'a') as file:
        file.write("\n")
        for data in donnees:
            file.write(str(data)+"\t\t")
   # print("Les données sont sauvgarder")
def destroyApp():
    client.disconnect()
client.loop_start()
client.on_message = on_message
            
if __name__ == "__main__":
    try:
         while True: 
            i=1
            while i<5:
                if message_finish:
                    get_data = "GET_DATA"+str(i)
                    client.publish("request",get_data)
                      
                    i=i+1
                    time.sleep(2)
            print("\n") 
    except:
        print("erreur.....")
        destroyApp()






































# import time
# import paho.mqtt.client as mqtt
# import json
# import threading
# # Configuration du broker MQTT
# broker_address = "localhost"
# broker_port = 1883
# excel_file = "data.txt"

# message_finish = True
# client = mqtt.Client()
# client.connect(broker_address, broker_port)
# client.subscribe("response")
# client.subscribe("response1")
# client.subscribe("response2")
# client.subscribe("response3")
# def on_message(client, userdata, message):
#         global message_finish
#         msg = message.topic
#         if msg == "response":
#             if not message_finish:
#                 return
#             else:
#                 message_finish = False
#                 donnees = str(message.payload.decode("utf-8","ignore"))
#                 donnees = json.loads(donnees)
#                 sauvegarder_donnees_excel(donnees,"data_noeud1.txt")  
#                 print("les données de noeud1 sont sauvegarder.")
#                 message_finish = True
#         elif msg == "response1":
#             if not message_finish:
#                 return
#             else:
#                 message_finish = False
#                 donnees = str(message.payload.decode("utf-8","ignore"))
#                 donnees = json.loads(donnees)
#                 sauvegarder_donnees_excel(donnees,"data_noeud2.txt")
#                 print("les données de noeud2 sont sauvegarder.")
#                 message_finish = True
#         elif msg == "response2":
#             if not message_finish:
#                 return
#             else:
#                 message_finish = False
#                 donnees = str(message.payload.decode("utf-8","ignore"))
#                 donnees = json.loads(donnees)
#                 sauvegarder_donnees_excel(donnees,"data_noeud3.txt")
#                 print("les données de noeud3 sont sauvegarder.")
#                 message_finish = True
#         elif msg == "response3":
#             if not message_finish:
#                 return
#             else:
#                 message_finish = False
#                 donnees = str(message.payload.decode("utf-8","ignore"))
#                 donnees = json.loads(donnees)
#                 sauvegarder_donnees_excel(donnees,"data_noeud4.txt")
#                 print("les données de noeud4 sont sauvegarder.")
#                 message_finish = True

# # def sauvegarder_donnees_excel(donnees,dataset):
# #     donnees = list(donnees)
# #     with open(dataset, 'a') as file:
# #         file.write("\n")
# #         for data in donnees:
# #             file.write(str(data)+",")
# #     print("Les données sont sauvgarder")

# def sauvegarder_donnees_excel(donnees, dataset):
#     donnees = list(donnees)
#     with open(dataset, 'a') as file:
#         file.write('\n')
#         for i, data in enumerate(donnees):
#             file.write(str(data))
#             if i < len(donnees) - 1:
#                 file.write(',')
#     print("Les données sont sauvegardées")
    
# def destroyApp():
#     client.disconnect()
# client.loop_start()
# client.on_message = on_message
            
# if __name__ == "__main__":
#     try:
#          while True: 
#             i=1
#             while i<5:
#                 if message_finish:
#                     get_data = "GET_DATA" + str(i)
#                     client.publish("request",get_data)
#                     print(get_data)
#                     print("publier \n")   
#                     i=i+1
#                     time.sleep(2)
#     except:
#         print("erreur.....")
#         destroyApp()