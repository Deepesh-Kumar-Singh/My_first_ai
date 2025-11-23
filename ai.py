import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from groq import Groq
import os
from config import api_key
chatStr = ""
def chat(query):
    global chatStr
    client = Groq(api_key=api_key)
    chatStr += f"deepesh: {query}\n Jarvis: "
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Free model
        messages=[{"role": "user", "content": query}])
    say(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    print(chatStr)
def ai(prompt):
    text=f"Jervis response for {prompt} \n ***********************************\n\n"
    client = Groq(api_key=api_key)

    response= client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Free model
        messages=[{"role": "user", "content": prompt}])

    text+=response.choices[0].message.content
    if not os.path.exists("Jervis"):
        os.mkdir("Jervis")
    with open(f"Jervis/{' '.join(prompt.split('intelligence')[1:] ).strip()}.txt", "w") as f:
        f.write(text)
    # say(response.content)
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"user said-{query}")
            return query
        except Exception as e:
            return "some error occured"


if __name__ == '__main__':
    print("pycahar")
    say("  hello I am  Jarvis")
    while True:
        print("listening.....")
        query=takecommand()
        sites=[["youtube","https://www.youtube.com"],["facebook","https://www.facebook.com"],["google","https://www.google.com"],["wikipidia","https://www.wikipidia.com"],["spotify","https://www.spotify.com"]]
        apps=[["project","PyCharm"],["calculator","calc"],["file","file explorer"],["browser","Microsoft edge"],["whatsapp","WhatsApp"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir...")
                webbrowser.open(f"{site[1]}")
        if f"open camera".lower() in query.lower():
            os.system("start microsoft.windows.camera:")
        elif f"the time".lower() in query.lower():
            time=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {time}")
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say(f"opening {app[0]} sir...")
                os.system(f"start {app[1]}")
        if "using Artificial Intelligence".lower() in query.lower():
            say(f"using Artificial Intelligence")
            ai(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
            os.system("clear")
        else:
            print("Chatting...")
            chat(query)




