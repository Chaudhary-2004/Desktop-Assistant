# Desktop-Assistant
Personal Desktop Assistant

# 🎙️ Shashwat's Voice Assistant

A Python-based desktop voice assistant that can recognize speech commands, speak responses, open applications, launch websites, search Gmail, play music, and perform basic desktop automation.

## ✨ Features

* 🎤 Speech recognition using microphone
* 🔊 Text-to-Speech responses
* 🌐 Open popular websites

  * YouTube
  * Google
  * GitHub
* 📧 Open Gmail
* 🔍 Search Gmail by

  * Subject
  * Sender / Organization
* 🎵 Play local music files
* 📝 Open Notepad
* 🧮 Open Calculator
* 🕒 Tell the current time
* 👋 Exit the assistant using voice commands

---

## 🛠️ Technologies Used

* Python 3.x
* SpeechRecognition
* PyAudio
* pyttsx3
* webbrowser
* os
* datetime

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2. Install dependencies

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

The assistant will greet you and begin listening for commands.

---

## 🎯 Supported Voice Commands

### Websites

| Voice Command | Action        |
| ------------- | ------------- |
| Open YouTube  | Opens YouTube |
| Open Google   | Opens Google  |
| Open GitHub   | Opens GitHub  |

---

### Applications

| Voice Command   | Action                          |
| --------------- | ------------------------------- |
| Open Notepad    | Opens Windows Notepad           |
| Open Calculator | Opens Windows Calculator        |
| Open Music      | Plays the configured music file |

---

### Gmail

Say:

```
Open Mail
```

The assistant asks:

```
Do you want to open a specific mail?
```

If you answer **Yes**, you can search by:

### Subject

Example:

```
Subject
```

then

```
Amazon Internship
```

The assistant searches Gmail for:

```
subject:Amazon Internship
```

---

### Sender

Example:

```
Sender
```

then

```
Google
```

The assistant searches Gmail for:

```
from:Google
```

---

### Time

Say:

```
What is the time?
```

or simply

```
Time
```

The assistant announces the current system time.

---

### Exit

Say:

```
Bye
```

The assistant closes gracefully.

---

## 📁 Project Structure

```
Voice-Assistant/
│
├── main.py
├── README.md
├── requirements.txt
└── assets/
```

---

## ⚙️ Configuration

### Change Music File

Update the path in:

```python
musicpath = r"C:\Users\Shash\Downloads\Deewanapan-Hai.mp3"
```

to any local music file.

---

### Add More Websites

Modify the list:

```python
sites = [
    ["youtube", "https://www.youtube.com"],
    ["google", "https://www.google.com"],
    ["github", "https://github.com"]
]
```

---

### Change Voice

```python
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
```

* `voices[0]` → Male voice
* `voices[1]` → Female voice (depends on installed Windows voices)

---

## 📌 Requirements

* Windows OS
* Python 3.9+
* Working microphone
* Internet connection (for speech recognition and web browsing)

---

## 🚀 Future Improvements

* Open any desktop application using voice
* Weather updates
* News headlines
* ChatGPT integration
* AI conversations
* Voice authentication
* Email sending
* WhatsApp automation
* Spotify control
* Volume and brightness control
* System shutdown/restart commands
* Reminder and alarm support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for educational and personal use.

---

## 👨‍💻 Author

**Shashwat Chaudhary**

Computer Science Engineer | Python Developer | AI & Machine Learning Enthusiast

If you found this project useful, consider giving the repository a ⭐.
