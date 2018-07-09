import logging
import paho.mqtt.client as mqtt
from json import dumps as jsonify
from enum import IntEnum
from gpiozero import DigitalOutputDevice
from dotenv import load_dotenv
from config import DEVICE
import os

from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=str(env_path), verbose=True)

SERVER = os.getenv('MQTT_SERVER')
PORT = int(os.getenv('MQTT_PORT'))
SECRET = os.getenv('SECRET')

headers = {'X-Secret': SECRET}
deviceId = DEVICE.get('deviceId')

# Logging setup
#log = open('lightberry.log')
logging.basicConfig(format='%(asctime)s %(message)s', filename='lightberry.log')

class Status(IntEnum):
    OFF = 0
    ON = 1

class Controller:
    def __init__(self, pin):
        self.__status = Status.OFF
        self.__device = DigitalOutputDevice(pin)

    def setStatus(self, status):
        if status == Status.OFF:
            self.__device.off()
        elif status == Status.ON :
            self.__device.on()
        self.__status = status
        return self.__status

    def getStatus(self):
        return self.__status

controller = Controller(23)

def registerDevice():
        payload = jsonify({
            'metadata': DEVICE,
            'state': controller.getStatus()
          })
        mqttc.publish("{}/online".format(deviceId), payload)

def publishStatus():
    payload = jsonify({
        'state': controller.getStatus()
      })
    mqttc.publish("{}/status".format(deviceId), payload)

def handleOnMessage(mosq, obj, msg):
    controller.setStatus(Status.ON)
    publishStatus()

def handleOffMessage(mosq, obj, msg):
    controller.setStatus(Status.OFF)
    publishStatus()

def handleConnect(mqttc, obj, flags, rc):
    registerDevice()
    mqttc.subscribe('{}/+'.format(deviceId), 0)
    mqttc.subscribe('host/+', 0)

def handleServerMessage(mosq, obj, msg):
    registerDevice()

def logMessage(mosq, obj, msg):
    logging.info('recieved message on %s', msg.topic)


#subscribe.callback(handleMessage, '{}/+'.format(deviceId), hostname=mqtt_server, port=mqtt_port)
mqttc = mqtt.Client(client_id=deviceId)

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add('*', logMessage)
mqttc.message_callback_add('{}/on'.format(deviceId), handleOnMessage)
mqttc.message_callback_add('{}/off'.format(deviceId), handleOffMessage)
mqttc.message_callback_add('host/online', handleServerMessage)

mqttc.on_connect = handleConnect
mqttc.connect(SERVER, PORT, 60)

pairingCode = DEVICE.get('pairingCode')
print("Connected. Pairing code: {}".format(pairingCode))

mqttc.loop_forever()
