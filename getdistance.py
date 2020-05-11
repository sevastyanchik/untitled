import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
broker = "srv1.mqtt.4api.ru"
port = 9124
username = "user_8d1a4972"
password = "pass_b576844d"
client = mqtt.Client("seva2")
client.username_pw_set(username, password)
client.connect(broker, port)

from time import sleep
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

    if distance <15 :
        client.publish("user_8d1a4972/sevahoma/0", "щт")
        print('on')
        for i in range(5):
            GPIO.output(16, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(16, GPIO.LOW)
            sleep(0.1)
