import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "mqtt/sampletopic"

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()}")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker successfully.")
        client.subscribe(topic)
    else:
        print(f"Failed to connect to MQTT Broker.")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

client.loop_forever()