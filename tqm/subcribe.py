import paho.mqtt.client as mqtt
import time

def on_message1(client,userdata,message):
    print("Received data : ", str( message.payload.decode('utf-8')))


mqttBroker = 'mqtt.eclipseprojects.io'
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPRETURE")
client.on_message = on_message1
time.sleep(30)
client.loop_stop()






