from threading import Thread

import paho.mqtt.client as mqtt

listener_pc = mqtt.Client()

msgFromPC = ""


class ListenPC(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        listener_pc.connect("192.168.1.9", 1883, 60)
        listener_pc.on_connect = self.on_connect
        listener_pc.on_message = self.on_message
        print("client is created")

    def run(self):
        print("pc_thread start")
        listener_pc.loop_forever()

    def disconnect(self):
        print("=====")
        listener_pc.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        listener_pc.subscribe("f")
        print("I am listening to pc")

    def on_message(self, client, userdata, msg):
        global msgFromPC
        msgFromPC = msg.payload.decode()


