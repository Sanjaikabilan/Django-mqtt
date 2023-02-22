import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Create an MQTT client object
client = mqtt.Client()

# Set the callback functions for MQTT events
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.username_pw_set(username="xxjfwlqo:xxjfwlqo", password="9agKXHW-5duIFt7ehaLp6JSM4-L-SMkc")
client.connect("fly.rmq.cloudamqp.com", 1883, 60)

# Subscribe to a topic
client.subscribe("abcd")

# Start the MQTT client loop
client.loop_start()

while True:
    client.publish("abcd", "56")

# Publish a message to a topic
