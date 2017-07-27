from gpiozero import MotionSensor 
from signal import pause
from time import sleep
import paho.mqtt.client as mqtt

import RPi.GPIO as GPIO
import time

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

motionsensor = MotionSensor(4)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) 
GPIO.setup(24, GPIO.OUT)

try:
    time.sleep(1.5) 
    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(0.5) 
            GPIO.output(24, False)
            print("You Are In My Spot...")
            time.sleep(1) 
        time.sleep(0.5) 
except:
    GPIO.cleanup()

def motionsensor():
	print("motion detected ")
	client.publish("test/motion", "detected")
try:
    mqtt.client
    while
         motionsensor.when_motion = motionsensor

pause()


