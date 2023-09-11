import paho.mqtt.client as mqtt
from random import randint , uniform
import time

mqtttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.connect(mqtttBroker)

while True:
    randNumber = uniform(20.0, 22.0)
    client.publish("TEMPRETURE", randNumber)
    print("just Published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)