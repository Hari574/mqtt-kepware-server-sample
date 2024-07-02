import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "mqtt/sampletopic"

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, port, 60)
client.subscribe(topic)

client.loop_forever()