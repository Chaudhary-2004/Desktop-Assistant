import speech_recognition as sr
import pyttsx3
import webbrowser
import cohere
import os
import datetime

co = cohere.Client(os.getenv("COHERE_API_KEY"))

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def say(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.5

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language="en-IN")
        print("You:", text)
        return text

    except sr.UnknownValueError:
        say("We were not able to listen")
        return None

    except Exception as e:
        print(e)
        say("We were not able to listen")
        return None

def chat(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt
        )

        ans = str(response.text)

        ans = ans.replace("**", "")
        ans = ans.replace("*", "")
        ans = ans.replace("#", "")
        ans = ans.replace("`", "")

        print(ans)

        for i in range(0, len(ans), 300):
            say(ans[i:i+300])

    except Exception as e:
        print(e)
        say("Sorry Sir, something went wrong.")

if __name__ == "__main__":

    say("Welcome to the Speech Recognition Program")
    say("Hello I am Shashwat's assistant")

    while True:

        text = recognize_speech_from_mic()

        if text is None:
            continue

        sites = [
            ["youtube", "https://www.youtube.com/"],
            ["google", "https://www.google.com/"],
            ["github", "https://github.com/"]
        ]

        handled = False

        for site in sites:
            if f"open {site[0]}" in text.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                say(f"{site[0]} opened Sir")
                handled = True
                break

        if handled:
            continue

        if "open music" in text.lower():
            say("Opening music")
            musicpath = r"C:\Users\Shash\Downloads\Deewanapan-Hai.mp3"
            os.startfile(musicpath)
            say("Music opened Sir")

        elif "open mail" in text.lower():
            say("Opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            say("Mail opened Sir")

            say("Do you want to open a specific mail?")

            while True:

                answer = recognize_speech_from_mic()

                if answer is None:
                    continue

                if "yes" in answer.lower():

                    say("Do you want to search by subject or sender?")

                    search_type = recognize_speech_from_mic()

                    if search_type is None:
                        continue

                    if "subject" in search_type.lower():

                        say("Please tell me the subject")

                        subject = recognize_speech_from_mic()

                        if subject is not None:
                            url = f"https://mail.google.com/mail/u/0/#search/subject%3A{subject.replace(' ','%20')}"
                            webbrowser.open(url)
                            say("Done")
                            break

                    elif "sender" in search_type.lower() or "organization" in search_type.lower() or "from" in search_type.lower():

                        say("Please tell me the sender")

                        sender = recognize_speech_from_mic()

                        if sender is not None:
                            url = f"https://mail.google.com/mail/u/0/#search/from%3A{sender.replace(' ','%20')}"
                            webbrowser.open(url)
                            say("Done")
                            break

                elif "no" in answer.lower():
                    say("Okay")
                    break

        elif "time" in text.lower():
            t = datetime.datetime.now().strftime("%H:%M")
            say(f"Current time is {t}")

        elif "open notepad" in text.lower():
            say("Opening Notepad")
            os.startfile(r"C:\Windows\System32\notepad.exe")

        elif "open calculator" in text.lower():
            say("Opening Calculator")
            os.startfile(r"C:\Windows\System32\calc.exe")

        elif "chat" in text.lower():

            say("What would you like to ask?")

            query = recognize_speech_from_mic()

            if query is not None:
                chat(query)
                

        elif "bye" in text.lower():
            say("Bye")
            break
