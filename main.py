from receive_message import Client
from groq import groq
import os
client = Client()
client.__init__()

def ping(body: str, phone_number: str):
    client.message.send("Pong")

def chat(body: str, phone_number: str):
    client.message.send(groq(os.getenv('GROQ_API_KEY'), ' '.join(client.msg.args)))

client.set_prefix("!")
client.add_command("ping", ping)
client.add_command("chat", chat)

client.start()