# 🎙️ Atlas – Python Voice Assistant

Atlas is a Python-based voice assistant that listens for a wake word and performs tasks like opening websites, reading news, telling weather, playing music, and answering questions.

---

## 🚀 Features

* 🎤 Wake word detection (“Atlas”)
* 🌐 Open websites (Google, YouTube, LinkedIn, GitHub, etc.)
* 🎵 Play local music or search Spotify
* 📰 Latest news headlines (NewsAPI)
* 🌦️ Weather updates
* 🕒 Time & Date announcements
* 🔊 Text-to-speech voice output

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* gTTS / pyttsx3
* Requests
* Webbrowser
* Geocoder
* OpenAI API
* NewsAPI

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/atlas-voice-assistant.git
cd atlas-voice-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Keys

Open `atlas.py` and replace:

```python
newsApi = "YOUR_NEWS_API_KEY"
weather_api = "YOUR_WEATHER_KEY"
```

Add your keys from:

* https://newsapi.org
* https://openweathermap.org

---

## ▶️ Run Atlas

```bash
python atlas.py
```

Say **“Atlas”** to activate, then speak your command.

---

## 📂 Project Structure

```
atlas-voice-assistant/
│── main.py
│── musicLibrary.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🌟 Future Improvements

* Jarvis-style continuous listening
* Face recognition login
* Voice memory system
* WhatsApp automation
* GUI interface

---

## 👨‍💻 Author

Made with ❤️ by *Anunay Chhapre*

---

## 📜 License

This project is open-source under the MIT License.

