import paho.mqtt.client as mqtt
import time
import json

broker = "localhost"
port = 1883
topic = "sampletopic"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker successfully.")
    else:
        print(f"Failed to connect to MQTT Broker.")

client.on_connect = on_connect

client.connect(broker, port, 60)

value = 0
while True:
    value = value + 1

    message = {"val1": value}
    client.loop_start()
    client.publish(topic,  payload=json.dumps(message))
    client.loop_stop()
    time.sleep(1)

client.disconnect()
