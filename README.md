# 🎤 Voice Assistant Project

A Python-based Voice Assistant with speech recognition, text-to-speech, and command processing capabilities. Two versions are provided: Basic and Advanced.

## 📋 Project Overview

This project implements a voice-controlled assistant that can:
- Recognize and process voice commands
- Convert text to speech for responses
- Perform various tasks (tell time, search web, get weather, etc.)
- Handle reminders and errors gracefully
- Provide a user-friendly interaction experience

## 🚀 Features

### Basic Version (`voice_assistant.py`)
- ✅ Speech Recognition (Google Speech API)
- ✅ Text-to-Speech Response
- ✅ Time & Date Information
- ✅ Web Search
- ✅ Joke Telling
- ✅ Help Command
- ✅ Error Handling

### Advanced Version (`voice_assistant_advanced.py`)
- ✅ All Basic Features
- ✅ Weather Information (Real-time data)
- ✅ Reminder System
- ✅ Natural Language Processing
- ✅ City-specific Weather Queries
- ✅ Reminder Checking
- ✅ Enhanced Error Handling

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- Microphone (for voice input)
- Speaker (for voice output)
- Internet connection

### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org)

### Step 2: Clone or Download the Project
```bash
# Download the project files to your desired location
cd voice-assistant
```

### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

**Or manually install:**
```bash
pip install SpeechRecognition==3.10.0
pip install pyttsx3==2.90
pip install requests==2.31.0
```

### Step 4: System-specific Setup (Optional)

**On Windows (with pyaudio):**
```bash
pip install pipwin
pipwin install pyaudio
```

**On macOS:**
```bash
# Using Homebrew
brew install portaudio
pip install pyaudio
```

**On Linux:**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## 💻 Usage

### Run Basic Version
```bash
python voice_assistant.py
```

### Run Advanced Version
```bash
python voice_assistant_advanced.py
```

## 🎤 Available Commands

### Time & Date
```
"What time is it?"
"What's the date?"
"Tell me the time"
```

### Web Search
```
"Search for [topic]"
"Google [query]"
"Search python tutorials"
```

### Weather (Advanced Only)
```
"What's the weather?"
"Weather in London"
"How's the weather in Paris?"
"Temperature in New York"
```

### Reminders (Advanced Only)
```
"Remind me to [task]"
"Set a reminder for [task] in 10 minutes"
"Check my reminders"
```

### Entertainment
```
"Tell me a joke"
"Make me laugh"
"Tell a joke"
```

### General
```
"Hello" or "Hi"
"Help" - Shows available commands
"Goodbye" or "Exit" - Closes the assistant
```

## 📁 Project Structure

```
voice-assistant/
├── voice_assistant.py              # Basic version
├── voice_assistant_advanced.py      # Advanced version
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🔑 Key Concepts Explained

### 1. Speech Recognition
- Uses Google's Speech Recognition API
- Converts audio input to text
- Handles ambient noise automatically

### 2. Text-to-Speech (TTS)
- Uses pyttsx3 library
- Converts assistant responses to audio
- Adjustable speech rate and voice properties

### 3. Command Processing
- Natural Language Processing (NLP) for command interpretation
- Keyword matching for command recognition
- Context-aware responses

### 4. Error Handling
- Timeout handling for unheard audio
- Network error management
- User-friendly error messages

### 5. Data Processing
- Regular expressions for number extraction
- String manipulation for query parsing
- List management for reminders

## 🌐 API Integration

### Weather API (Advanced Version)
- Uses Open-Meteo API (free, no API key required)
- Provides real-time weather data
- Supports multiple locations

### Search Engine
- Integrates with Google Search
- Opens results in default browser

## 🛠 Customization

### Change Voice Properties
```python
self.engine.setProperty('rate', 150)  # Speed (default: 150)
self.engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
```

### Add New Commands
Add new methods and expand the `process_command()` function:
```python
elif "your command" in command:
    self.your_new_method()
```

### Modify Jokes
Edit the `jokes` list in the `tell_joke()` method.

### Change Default Location
```python
def get_weather(self, city="Your City"):
    # ...
```

## ⚠️ Troubleshooting

### "No microphone found"
- Check if microphone is properly connected
- Test microphone in system settings
- Use `python -m speech_recognition` to test

### "Could not request results from Google"
- Check internet connection
- Try again in a few moments
- Check if Google API is accessible in your region

### "Error initializing microphone"
- Install pyaudio: `pip install pyaudio`
- Check system audio settings
- Restart the application

### "Speech not recognized"
- Speak clearly and closer to microphone
- Reduce background noise
- Try again or say "help"

## 🚀 Advanced Features to Implement

### For Future Development:
1. **Email Integration** - Send emails via voice commands
2. **Calendar Integration** - Check and set calendar events
3. **Smart Home Control** - Control IoT devices
4. **Music Player** - Play music on command
5. **News Updates** - Get latest news
6. **Calculator** - Voice-based calculations
7. **Database** - Store conversation history
8. **Multi-language Support** - Support multiple languages
9. **Custom Wake Word** - Activate with specific phrase
10. **GUI Interface** - Visual interface for the assistant

## 📚 Learning Resources

- **Speech Recognition**: [SpeechRecognition Docs](https://github.com/Uberi/speech_recognition)
- **Text-to-Speech**: [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- **Python NLP**: [NLTK Documentation](https://www.nltk.org/)
- **Web APIs**: [Python Requests Library](https://requests.readthedocs.io/)

## 🔐 Security & Privacy

- **Microphone Access**: Ensure you have proper permissions
- **Voice Data**: Processed locally first, then sent to Google API for recognition
- **Search History**: Browser search queries are not stored by the assistant
- **Personal Information**: Be cautious with voice commands containing sensitive data

## 📝 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📧 Support

For issues and questions:
1. Check the Troubleshooting section
2. Review error messages in the console
3. Test with the basic version first
4. Ensure all dependencies are installed

## 🎯 Next Steps

1. **Run the basic version** to get familiar with the assistant
2. **Test available commands** to understand functionality
3. **Customize as needed** for your use case
4. **Explore advanced version** for additional features
5. **Implement your own enhancements**

---

**Created:** June 2026
**Python Version:** 3.7+
**Status:** Fully Functional ✅

Enjoy your Voice Assistant! 🎤🤖
