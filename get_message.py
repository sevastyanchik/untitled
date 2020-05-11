import paho.mqtt.client as mqtt

from time import sleep


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("dist")
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    distanse = float(message)
    if distanse < 15:
        client.publish('to_PRi', 'stop')
        print('stop')

    print(message)
# client.disconnect()
broker = "192.168.1.9"
port = 9124
# username = "user_8d1a4972"
# password = "pass_b576844d"
client = mqtt.Client()
# client.username_pw_set(username, password)
client.connect(broker,1883,1000 )
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
