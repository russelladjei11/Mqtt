from gpiozero import  MotionSensor

 
from signal import pause
from time import sleep
import paho.mqtt.client as mqtt


client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

motionsensor = MotionSensor(4)

def motionsensor_motion_detected():
	print("motion detected ")
	client.publish("test/motion", "detected")

def when_pressed():
	print("button pressed")

motionsensor.when_motion = motionsensor_motion_detected
pause()


