from gpiozero import MotionSensor
from time import sleep
import paho.mqtt.client as mqtt
from time import sleep

def motionsenor(client, userdata, flags, code):
	print "connected: " + str(code)
	client.publish("test/motion")
def motionsensor():
        print("motion detected ")
        client.publish("test/motion", "detected")

client = mqtt.Client()
client.on_connect = motionsensor


client.connect("broken.hivemq.com", 1883, 60)
client.loop_forever
