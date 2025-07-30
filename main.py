import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import pygetwindow as gw
import time
import pyperclip
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

r = sr.Recognizer()
engine = pyttsx3.init()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def speak(s):
    engine.say(s)
    engine.runAndWait()


def processcommand(command):
    if "whatsapp" in command.lower():
        whatsapp_window_found = False
        for window in gw.getAllWindows():
            title = window.title.lower()
            if "whatsapp" in title:
                whatsapp_window_found = True
                if not window.isActive:
                    speak("Switching to WhatsApp")
                    time.sleep(1.5)
                    window.restore()
                    window.activate()
                    speak("Tell me the contact you want to chat with")
                    search_and_open_contact()
                else:
                    speak("Already on WhatsApp")
                    speak("Tell me the contact you want to chat with")
                    search_and_open_contact()
                return
        
        if not whatsapp_window_found:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com/")
            speak("Tell me the contact you want to chat with")
            search_and_open_contact()

def search_and_open_contact():
    max_attempts = 3
    for _ in range(max_attempts):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
                contact = r.recognize_google(audio)
                pyautogui.click(281,212)
                pyautogui.typewrite(contact,interval=0.1)
                time.sleep(2)
                
                try:
                    not_found = pyautogui.locateOnScreen("Screenshot 2025-06-30 103627.PNG",confidence=0.7)
                except pyautogui.ImageNotFoundException:
                    print("Couldn't Find the contact")
                    not_found=None

                if not_found is None:
                    speak(f"Opening chat with {contact}")
                    pyautogui.press("enter")
                    Replying("PREET SHAH")
                    break
                else:
                    speak("Try again")
                    pyautogui.press("esc")
                    continue
        except sr.WaitTimeoutError:
            print("Listening timed out — no speech detected in time.")
        except sr.UnknownValueError:
            print("Chatbot could not understand audio")
        except sr.RequestError as e:
            print("Audio error; {0}".format(e))

# Giving further task to openAI to reply automatically



# Checks who sent the last message
def last_sender(chat, your_name):
    lines = chat.strip().splitlines()
    for line in reversed(lines):
        if "] " in line and ": " in line:
            try:
                sender_line = line.split("] ", 1)[1]
                sender = sender_line.split(": ", 1)[0].strip()
                return sender
            except:
                continue
    return None

# Monitors chat and replies when contact sends a new message
def Replying(your_name):
    last_seen = ""

    while True:
        # Copy chat content
        pyautogui.moveTo(700, 207)
        pyautogui.dragTo(700, 1013, duration=2, button="left")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)
        raw_chat = pyperclip.paste()
        pyautogui.click(700, 1013)

        sender = last_sender(raw_chat, your_name)
        if sender != your_name and raw_chat != last_seen:
            # Clean message text
            lines = raw_chat.strip().splitlines()
            messages = []
            for line in lines:
                if "] " in line and ": " in line:
                    try:
                        _, content = line.split("] ", 1)
                        _, message = content.split(": ", 1)
                        messages.append(message.strip())
                    except:
                        continue
            plain_history = "\n".join(messages).strip()

            # Send to GPT
            
            

            

            try:
                response = client.chat.completions.create(
                    model="gpt-4-1106-preview",
                    messages=[
                        {"role": "system", "content": "You are a person named Preet. Reply casually."},
                        {"role": "user", "content": plain_history}
                    ]
                )
                reply = response.choices[0].message.content.strip()
            except Exception as e:
                reply = "Sorry, I couldn't generate a reply right now."
                print(f"OpenAI error: {e}")



            # Send reply
            pyautogui.click(797, 975)
            pyautogui.typewrite(reply)
            pyautogui.press("enter")
            print("Replied.")

            last_seen = raw_chat

        else:
            print("Waiting...")

        time.sleep(5)  # wait before checking again




                        
     

if __name__=="__main__":

    speak("Initializing Chatbot")
    while True:
            
                
    # recognize speech using google
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Listening...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=5)

                word = r.recognize_google(audio)
                print(word)
                if word.lower() == "reply":
                    speak("Please tell me the application")
                    #Waiting for command
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source) # Records
                        command = r.recognize_google(audio) #converts 
                        print(command)
                        processcommand(command)


            except sr.WaitTimeoutError:
                print("Listening timed out — no speech detected in time.")
            except sr.UnknownValueError:
                print("Chatbot could not understand audio")
            except sr.RequestError as e:
                print("Audio error; {0}".format(e))