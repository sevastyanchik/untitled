import paho.mqtt.client as mqtt
broker = "srv1.mqtt.4api.ru"
port = 9124
username = "user_8d1a4972"
password = "pass_b576844d"
client = mqtt.Client("seva2")
client.username_pw_set(username, password)
client.connect(broker, port)
client.publish("user_8d1a4972/sevahoma/0", "110111")
