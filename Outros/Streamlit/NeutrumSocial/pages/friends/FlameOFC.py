import streamlit as st
import json
import requests
from datetime import datetime

friend_name = "FlameOFC"
agora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

with open('./data/login.json', 'r') as arquivo:
    username = json.load(arquivo)["user"]["username"]


r = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/chat/{friend_name}/friend/.json").json()

if r == "'":
    friend_messages = 0
else:
    friend_messages = len(r)
st.write(friend_messages)


DATABASE = f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/chat/{friend_name}/you/.json"
r = requests.get(DATABASE)
json_data = r.json()

my_messages = len(json_data)
st.write(my_messages)


message = st.chat_input('Digite sua mensagem aqui')

you = st.chat_message("user", avatar=":material/account_circle:")
you.caption('Você')

for _, mensagem in json_data.items():
    you.write(mensagem)

if message:
    with you:
        DATABASE = f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/chat/{friend_name}/you/.json"

        data = {
            agora: message,
        }

        r = requests.patch(DATABASE, json=data)


friend = st.chat_message("assistant", avatar=":material/mood:")
with friend:
    st.caption(friend_name)
    st.write("oi")
