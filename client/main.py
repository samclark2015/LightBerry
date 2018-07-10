import logging, os, sys
import paho.mqtt.client as mqtt
from importlib import import_module
from json import dumps as jsonify

SERVER = os.getenv('MQTT_SERVER')
PORT = int(os.getenv('MQTT_PORT'))
SECRET = os.getenv('SECRET')

headers = {'X-Secret': SECRET}

deviceClass = os.getenv('DEVICE_CLASS')
Device = import_module('{}.device'.format(deviceClass)).Device

device = Device()

# Logging setup
logging.basicConfig(format='%(asctime)s %(message)s', filename='/var/log/lightberry.log')

def publishStatus():
    payload = jsonify({
        'state': device.getStatus()
    })
    mqttc.publish("{}/status".format(device.getId()), payload)

def handleConnect(mqttc, obj, flags, rc):
    mqttc.subscribe('host/+', 0)
    mqttc.subscribe('{}/+'.format(device.getId()), 0)
    device.registerMqtt(mqttc)

def handleServerMessage(mosq, obj, msg):
    device.registerMqtt(mqttc)

def logMessage(mosq, obj, msg):
    logging.info('recieved message on %s', msg.topic)


mqttc = mqtt.Client(client_id=device.getId())

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add('*', logMessage)
mqttc.message_callback_add('host/online', handleServerMessage)

mqttc.on_connect = handleConnect
mqttc.connect(SERVER, PORT, 60)

mqttc.loop_forever()