import paho.mqtt.client as mqtt

broker = "localhost"
port = "1883"
topic = "mqtt/sampletopic"

client = mqtt.Client()
client.connect(broker, port, 60)

message = "Hello.. This is sample MQTT"
client.publish(topic, message)

client.disconnect()
