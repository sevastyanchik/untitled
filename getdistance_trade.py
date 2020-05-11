import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import Listener as ls
from Listener import *

ls.msgFromPC = ''
pc_thread = ListenPC("Listen to PC")
pc_thread.start()

client = mqtt.Client()
client.connect("192.168.1.9", 1883, 1000)



LED = 16
TRIG = 21
ECHO = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
while True:
    pulse_start, pulse_end = 0, 0
    GPIO.output(TRIG, False)
    time.sleep(1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distanse:", distance, "cm")
    client.publish("dist", distance)
    if ls.msgFromPC == "stop":
        break

