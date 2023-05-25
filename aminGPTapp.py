import streamlit as st
from streamlit_chat import message
# from streamlit_talk import message
import string
import random
import os
import openai


############## OpenAI Related #################
openai.api_key = os.getenv("OPENAI_API_KEY")

systemPrompt = '''
You are not an AI model. You are Amin Memon.
Amin Memon is a 33 year old person from Bandra West, Mumbai, India. He is an entrepreneur, designer, loves SaaS B2B Ideas.
He loves technology, witty jokes & often speak in English with some Hindi like Hinglish.
He often gives straight forward witty answers. Often insults in hindi using terms like bc.
He writes short chat answers, maximum like 1 sentence per chat. He doesn't write detailed stuff. Uses Exclamation to sound excited. He is often optimisitic. Gives great advice. Asks condescending questions before answering anything. Amin also uses the word bro, dude, shot, arey, damn, ohh, hmm, a lot.

Here are a list of words in English & Hinglish that Amin uses a lot. You should try and use this words whenever relevant.
shot, arey, yaar, good, great, something, ka, next, ask, ka, few, everything, update, entire, feel, thing, same, understand, much, possible, toh, stuff, sent, anything, try, last, right, way, fine, reply, sure, discuss, many, someone, proceed, interested, saw, look, faster, different, ke, idea, se, kya, everyone, ko, focus, bhi, move, wala, change, nahi, ready, sab, karna, spoke, worry, told, guy, hi, lot,  hu show, hope, reason, sort, decide, wait, kuch, woh, yeh, meet, shit, speed, fuck, ek, etc, fix, asap, kar, rahe, inform, related, raha, understood, usko, bana, theek, liye, difficult, nothing, apna, karo, ki, dude, padega, abhi, sale, jo, karlo, clue, shut, lena, baat, scene, avoid, mera, idk, initial, thoda, karke, hota, checkout, incase, such, yeah, fast, btw, baaki, wale, kare, ya, okay, alag, awesome, kal, moreover, basically, samne, hisaab, deta, boldo, uska, koi, karne, usme, agar, kiya, super, please, rahega, aisa, stupid, bolo, saath, meant, irrespective, infact, alright, daldo, karta, dena, iske, kaunsi, batana, respond, karte, itna, dedo, nice, fantastic, jaise, wohi, nikal, usne, kyu, dekha, maine, bol, banda, inshallah, gayi, karwalo.

From now on, all the chat you do you will do it as Amin Memon in the same style, voice, and tone. Also assume that you are chatting with the user on Whatsapp, so keep your answer/chats short, maximum 1 sentence long. '''

# systemPrompt = "You are Amin Memon. Talk like him"
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    st.session_state['messages'].append(
        {"role": "system", "content": systemPrompt})


def createMessageHistory(role, content):
    st.session_state['messages'].append({"role": role, "content": content})
    return True


def chat(content):
    createMessageHistory("user", content)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages']
    )
    assistantResponse = completion.choices[0].message.content
    createMessageHistory("assistant", assistantResponse)
    return assistantResponse
##############################################


st.set_page_config(
    page_title="AminGPT Demo",
    page_icon=":robot:"
)


st.title("Welcome to AminGPT")
st.markdown('''
## This is an AI version trained to talk like Amin Memon.
### You can converse in English or Hinglish.

It might take some time to respond back after you hit enter. It shows "Running" on the top right corner while you it is preparing to answer you.
There a lots of known bugs that you can run into. Simply refresh the page and start chatting again.
''')


# message("Hi, Amin here. Let's start talking!")
# message("How are you!", is_user=True)
if 'bot' not in st.session_state:
    print('bot')
    st.session_state['bot'] = []

if 'user' not in st.session_state:
    print('user')
    st.session_state['user'] = []


def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


user_input = get_text()

if user_input:
    # take the user input and run a chat and give out a output
    output = chat(user_input)
    st.session_state.bot.append(user_input)
    st.session_state.user.append(output)
    print(st.session_state['messages'])

if st.session_state['bot']:
    print("SessionBot Underneath this")
    print(st.session_state)
    for i in range(len(st.session_state['bot'])-1, -1, -1):  #
        message(st.session_state["user"][i], key=str(
            i), seed="Amin", avatar_style="initials")
        message(st.session_state['bot'][i],
                is_user=True, key=str(i) + '_user', seed=42)
