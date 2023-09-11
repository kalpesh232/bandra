import paho.mqtt.client as mqtt
from random import random, randrange
import time

mqttBroker = 'mqtt.eclipseprojects.io'
client =  mqtt.Client('Temperature_Outside')
client.connect(mqttBroker)


while True:
    randNumber = randrange(10)
    client.publish("TEMPRETURE",randNumber)
    print("just Published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
