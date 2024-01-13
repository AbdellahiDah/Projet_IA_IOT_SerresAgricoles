import paho.mqtt.client as mqtt
from flask import Flask, render_template, request ,jsonify
import json, sqlite3, time, threading, numpy
import pandas as pd
import cv2
from flask import Flask, render_template, Response


app = Flask(__name__)
WAIT_SECONDS = 1
MAXTEMP = 40

data_node1 = pd.read_csv('data_noeud1.txt', delimiter=',',header=0)
data_node2 = pd.read_csv('data_noeud2.txt', delimiter=',',header=0)
data_node3 = pd.read_csv('data_noeud3.txt', delimiter=',',header=0)
data_node4 = pd.read_csv('data_noeud4.txt', delimiter=',',header=0)
data_node5 = pd.read_csv('node5.txt', delimiter=',' , header=0)


pins = {
       3 : {'name' : 'vert', 'board' : 'esp8266', 'topic' : 'esp8266/4', 'state' : 'False'},
       4 : {'name' : 'orange', 'board' : 'esp8266', 'topic' : 'esp8266/5', 'state' : 'False'},
       5 : {'name' : 'rouge', 'board' : 'esp8266', 'topic' : 'esp8266/6', 'state' : 'False'},
       }


camera = cv2.VideoCapture(0)  # Initialize camera (0 represents the default camera)

def generate_frames():
    while True:
        success, frame = camera.read()  # Read a frame from the camera
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame as JPEG
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield the frame as a response


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data',methods=['GET', 'POST'])
def dataTemp():
    return readData()


def readData():
    # temperature
    temperature1=data_node1.temperature
    temperature2=data_node2.temperature
    temperature3=data_node3.temperature
    temperature4=data_node4.temperature
    temperature5=data_node5.temperature
    
    moyen1=round(data_node1.temperature.mean(),2)
    moyen2=round(data_node2.temperature.mean(),2)
    moyen3=round(data_node3.temperature.mean(),2)
    moyen4=round(data_node4.temperature.mean(),2)
    moyen5=round(data_node5.temperature.mean(),2)
    moyenG = round((moyen1 + moyen2 + moyen3 + moyen4 + moyen5)/5,2)
    
    # Hum
    hum1=data_node1['humidite']
    hum2=data_node2['humidite']
    hum3=data_node3['humidite']
    hum4=data_node4['humidite']
    hum5=data_node5['humidite']
    moyhum1=round(data_node1['humidite'].mean(),2)
    moyhum2=round(data_node2['humidite'].mean(),2)
    moyhum3=round(data_node3['humidite'].mean(),2)
    moyhum4=round(data_node4['humidite'].mean(),2)
    moyhum5=round(data_node5['humidite'].mean(),2)
    moyhumG = round((moyhum1 + moyhum2 + moyhum3 + moyhum4 + moyhum5)/5,2)
    
   
    # CO2
    CO21=data_node1['CO2']
    CO22=data_node2['CO2']
    CO23=data_node3['CO2']
    CO24=data_node4['CO2']
    CO25=data_node5['CO2']
    moyco21=round(data_node1['CO2'].mean(),2)
    moyco22=round(data_node2['CO2'].mean(),2)
    moyco23=round(data_node3['CO2'].mean(),2)
    moyco24=round(data_node4['CO2'].mean(),2)
    moyco25=round(data_node5['CO2'].mean(),2)
    moyco2G = round((moyco21 + moyco22 + moyco23 + moyco24 + moyco25)/5,2)
   
    
    # CO2
    PH1=data_node1['PH']
    PH2=data_node2['PH']
    PH3=data_node3['PH']
    PH4=data_node4['PH']
    PH5=data_node5['PH']
    moyph1=round(data_node1['PH'].mean(),2)
    moyph2=round(data_node2['PH'].mean(),2)
    moyph3=round(data_node3['PH'].mean(),2)
    moyph4=round(data_node4['PH'].mean(),2)
    moyph5=round(data_node5['PH'].mean(),2)
    moyphG = round((moyph1 + moyph2 + moyph3 + moyph4 + moyph5)/5,2)
    
    
    
    # Convertir les objets Series en listes
    temperature1 = temperature1.tolist()
    temperature2 = temperature2.tolist()
    temperature3 = temperature3.tolist()
    temperature4 = temperature4.tolist()
    temperature5 = temperature5.tolist()

    hum1 = hum1.tolist()
    hum2 = hum2.tolist()
    hum3 = hum3.tolist()
    hum4 = hum4.tolist()
    hum5 = hum5.tolist()

    CO21 = CO21.tolist()
    CO22 = CO22.tolist()
    CO23 = CO23.tolist()
    CO24 = CO24.tolist()
    CO25 = CO25.tolist()

    PH1 = PH1.tolist()
    PH2 = PH2.tolist()
    PH3 = PH3.tolist()
    PH4 = PH4.tolist()
    PH5 = PH5.tolist()
    leds=[0,0,0]
    return jsonify(temperature1=temperature1,
                    temperature2=temperature2,
                    temperature3=temperature3,
                    temperature4=temperature4,
                    temperature5=temperature5,
                    moyen1=moyen1,
                    moyen2=moyen2,
                    moyen3=moyen3,
                    moyen4=moyen4,
                    moyen5=moyen5,
                    moyenG=moyenG,
                    hum1=hum1,
                    hum2=hum2,
                    hum3=hum3,
                    hum4=hum4,
                    hum5=hum5,
                    moyhum1=moyhum1,
                    moyhum2=moyhum2,
                    moyhum3=moyhum3,
                    moyhum4=moyhum4,
                    moyhum5=moyhum5,
                    moyhumG=moyhumG,
                    CO21=CO21,
                    CO22=CO22,
                    CO23=CO23,
                    CO24=CO24,
                    CO25=CO25,
                    moyco22=moyco22,
                    moyco23=moyco23,
                    moyco24=moyco24,
                    moyco25=moyco25,
                    moyco21=moyco21,
                    moyco2G=moyco2G,
                    PH1=PH1,
                    PH2=PH2,
                    PH3=PH3,
                    PH4=PH4,
                    PH5=PH5,
                    moyph1=moyph1,
                    moyph2=moyph2,
                    moyph3=moyph3,
                    moyph4=moyph4,
                    moyph5=moyph5,
                    moyphG=moyphG,
                    leds=leds)

 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8181, debug=True)
    
    
    
    



#mqttc=mqtt.Client()
#mqttc.on_connect = on_connect
#mqttc.on_message = on_message
#mqttc.connect("127.0.0.1",1883,60)
#mqttc.loop_start()

  
    
    
    

# def on_connect(client, userdata, flags, rc):
#     client.subscribe("/esp8266/1/temperature")
#     client.subscribe("/esp8266/2/temperature")
#     client.subscribe("/esp8266/3/temperature")
#     client.subscribe("/esp8266/4/temperature")
#     client.subscribe("/esp8266/5/temperature")

# def on_message(client, userdata, message):
#     if message.topic == "/esp8266/1/temperature" or message.topic == "/esp8266/2/temperature" or message.topic == "/esp8266/3/temperature" or message.topic == "/esp8266/4/temperature" or message.topic == "/esp8266/5/temperature" :
#         temperature = message.payload.decode("utf-8")
#         conn=sqlite3.connect('sensordata.db')
#         c=conn.cursor()
#         if message.topic == "/esp8266/1/temperature" : device="esp8266/1"
#         if message.topic == "/esp8266/2/temperature" : device="esp8266/2"
#         if message.topic == "/esp8266/3/temperature" : device="esp8266/3"
#         if message.topic == "/esp8266/4/temperature" : device="esp8266/4"
#         if message.topic == "/esp8266/5/temperature" : device="esp8266/5"
#         c.execute("""INSERT INTO dhtreadings (temperature,humidity,currentdate,currentime,device) 
#                 VALUES((?), (?), date('now'),time('now'), (?))""", (temperature, temperature, device) )
#         conn.commit()
#         conn.close() 
    
    
#if moyenG <= 15 :
    #         mqttc.publish(pins[3]['topic'],"1")
    #         mqttc.publish(pins[4]['topic'],"0")
    #         mqttc.publish(pins[5]['topic'],"0")
    #         leds[0]=0
    #         leds[1]=1
    #         leds[2]=0
    #         pins[3]['state'] = 'True'
    #         pins[4]['state'] = 'False' 
    #         pins[5]['state'] = 'False' 
    # elif moyenG > 15: 
    #         mqttc.publish(pins[4]['topic'],"1")
    #         mqttc.publish(pins[3]['topic'],"0")
    #         mqttc.publish(pins[5]['topic'],"0")
    #         leds[0]=1
    #         leds[1]=0
    #         leds[2]=0
    #         pins[4]['state'] = 'True' 
    #         pins[3]['state'] = 'False'
    #         pins[5]['state'] = 'False' 
    # else: 
    #         mqttc.publish(pins[5]['topic'],"1")
    #         mqttc.publish(pins[4]['topic'],"0")
    #         mqttc.publish(pins[3]['topic'],"0")
    #         leds[0]=0
    #         leds[1]=0
    #         leds[2]=1
    #         pins[5]['state'] = 'True' 
    #         pins[3]['state'] = 'False' 
    #         pins[4]['state'] = 'False'