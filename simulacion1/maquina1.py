#extraccion y envio de datos

#librerias
import csv
import json
import paho.mqtt.client as mqtt
import sys

#funciones mqtt
def on_connect(client, userdata, flags, rc):
	print("Connected with result code: "+str(rc))
	client.subscribe("retoDiversius123",qos=1)

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	if str(msg.payload) == "datosRecibidos":
		sys.exit("datos enviados correctamente")
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

#funcion envio datos
def envio():
	#reader = csv.reader(open('datos.csv', 'rb'), delimiter=';')
	reader = csv.reader(open('datos.csv', 'r'), delimiter=';')
	data='';
	for index,row in enumerate(reader):
		#data += 'Linea'+str(index +1)+':'+row[0]+','+row[1]+','+row[2]+','+row[3]+'\n'
		data += 'Maquina1'+row[0]+','+row[1]+','+row[2]+';'
	print (str(data))
	client.publish("retoDiversius123",data)
	print ("enviados")

envio()

#loop para recibir mensajes via mqtt
client.loop_forever()