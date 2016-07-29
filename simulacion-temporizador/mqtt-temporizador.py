#extraccion y envio de datos

#librerias
import paho.mqtt.client as mqtt
import sys
import random
import threading
from threading import Timer

#funciones mqtt
def on_connect(client, userdata, flags, rc):
	print("Connected with result code: "+str(rc))
	client.subscribe("retoDiversius123",qos=1)

def on_message(client, userdata, msg):
	#print(msg.topic+" "+str(msg.payload))
	if str(msg.payload) == "datosRecibidos":
		sys.exit("datos enviados correctamente")
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

#funcion envio datos
def envio():
	threading.Timer(2.0, envio).start()
	#data=random.randint(175, 290);
	data='maquina1';
	
	for x in range(3):
	    if x == 3:
	        break
	    data += ',%s' % random.randint(175, 290);
	
	print (data)
	client.publish("retoDiversius123",data)

envio()

#loop para recibir mensajes via mqtt
client.loop_forever()