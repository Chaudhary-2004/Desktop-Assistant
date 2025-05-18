import speech_recognition as sr
import pyttsx3 # os functionality does not work on Windows instead use pyttsx3
import webbrowser # for opening browser and searching
import openai
import os
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)     # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change voice
    engine.say(text)
    engine.runAndWait()
    
    
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    #if we want a pause threshold that ki humara assistant kitna der tak chalna chahiye
    recognizer.pause_threshold = 0.5
    with mic as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='en-IN') #language='en-IN' for Indian accent you can also use hi-in for Hindi
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None



if __name__ == "__main__":
    print("Welcome to the Speech Recognition Program!")
    say("Welcome to the Speech Recognition Program!")
    say("Hello I am Shashwat    's assistant")
    while(True):
        print("Listening...")
        text = recognize_speech_from_mic()
        sites=[["youtube","https://www.youtube.com/"], ["google","https://www.google.com/"], ["github","https://github.com/"]]
        for site in sites:
            if text is not None:
                if f"open {site[0]}" in text.lower():
                    print(f"Opening {site[0]}...")
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                    say(f"{site[0]} opened Sir")
                    break
        if text is not None:
            if "open music" in text.lower():
                print("Opening music...")
                say("Opening music")
                musicpath=r"C:\Users\Shash\Downloads\Deewanapan-Hai.mp3"
                os.startfile(musicpath)
                say("Music opened Sir")
            if "open mail" in text.lower():
                print("Opening mail...")
                say("Opening mail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                say("Mail opened Sir")
                
                # Ask if the user wants to open a specific mail
                say("Do you want to open a specific mail?")
                while True:
                    answer = recognize_speech_from_mic()
                    if answer is not None:
                        if "yes" in answer.lower():
                            print("Opening specific mail...")
                            say("Opening specific mail")

                            # Ask if by subject or sender
                            say("Do you want to search by subject or sender?")
                            search_type = recognize_speech_from_mic()

                            if search_type is not None:
                                if "subject" in search_type.lower():
                                    say("Please tell me the subject of the mail you want to open")
                                    subject = recognize_speech_from_mic()
                                    if subject is not None:
                                        print(f"Searching for mails with subject: {subject}")
                                        say(f"Searching for mails with subject: {subject}")
                                        formatted_subject = subject.replace(" ", "%20")
                                        search_url = f"https://mail.google.com/mail/u/0/#search/subject%3A{formatted_subject}"
                                        webbrowser.open(search_url)
                                        say(f"Mails with subject {subject} opened Sir")
                                        break

                                elif "sender" in search_type.lower() or "organization" in search_type.lower() or "from" in search_type.lower():
                                    say("Please tell me the sender or organization email or name")
                                    sender = recognize_speech_from_mic()
                                    if sender is not None:
                                        print(f"Searching for mails from: {sender}")
                                        say(f"Searching for mails from: {sender}")
                                        formatted_sender = sender.replace(" ", "%20")
                                        search_url = f"https://mail.google.com/mail/u/0/#search/from%3A{formatted_sender}"
                                        webbrowser.open(search_url)
                                        say(f"Mails from {sender} opened Sir")
                                        break

                                else:
                                    say("Sorry, I didn't understand. Please say subject or sender.")
                                    continue

                        elif "no" in answer.lower():
                            print("Okay")
                            say("Okay")
                            break
                    else:
                        continue


            if "time" in text.lower():
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                print(f"Current time is {current_time}")
                say(f"Current time is {current_time}")
            
            if "Open notepad".lower() in text.lower():
                print("Opening notepad...")
                say("Opening notepad")
                os.startfile(r"C:\Windows\System32\notepad.exe")
                say("Notepad opened Sir")
            if "open calculator".lower() in text.lower():  
                print("Opening calculator...")
                say("Opening calculator")
                os.startfile(r"C:\Windows\System32\calc.exe")
                say("Calculator opened Sir")
            if "Bye".lower() in text.lower():
                print("Bye")
                say("Bye")
                break
                
            

        
    
        
                
            
        
        
