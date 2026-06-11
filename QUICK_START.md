# ⚡ Quick Start Guide - Voice Assistant

Get your Voice Assistant running in 5 minutes!

## 🚀 Quick Setup

### 1️⃣ Install Python Packages (30 seconds)
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install SpeechRecognition pyttsx3 requests
```

### 2️⃣ Check Your Microphone
Make sure your microphone is:
- ✅ Connected and working
- ✅ Not muted
- ✅ Set as default input device

### 3️⃣ Run the Assistant
```bash
# For beginners:
python voice_assistant.py

# For advanced features:
python voice_assistant_advanced.py
```

### 4️⃣ Start Talking!
Once you see "🎤 Listening..." - speak your command clearly.

---

## 🎤 Commands Cheat Sheet

```
TIME & DATE:
- "What time is it?"
- "What's the date?"

SEARCH:
- "Search for Python programming"
- "Google machine learning"

WEATHER (Advanced Only):
- "What's the weather?"
- "Weather in London"

REMINDERS (Advanced Only):
- "Remind me to call mom"
- "Set reminder in 5 minutes"

FUN:
- "Tell me a joke"

CONTROL:
- "Help" → See all commands
- "Goodbye" → Exit assistant
```

---

## ⏱️ Common Commands Examples

### Example 1: Check Time
```
YOU: "What time is it?"
ASSISTANT: "The current time is 02:30 PM"
```

### Example 2: Search Web
```
YOU: "Search for Python tutorials"
ASSISTANT: "Searching for Python tutorials"
[Opens Google search results in browser]
```

### Example 3: Get Weather (Advanced)
```
YOU: "Weather in New York"
ASSISTANT: "Getting weather information for New York"
"In New York, it's currently 72 degrees with 60 percent humidity."
```

### Example 4: Set Reminder (Advanced)
```
YOU: "Remind me to drink water in 10 minutes"
ASSISTANT: "Reminder set for 10 minutes from now: drink water"
```

---

## 🆘 Quick Troubleshooting

### ❌ "No microphone detected"
```bash
# Test microphone:
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_indexes())"

# Should show your microphone. If not:
# 1. Check Windows/Mac/Linux sound settings
# 2. Restart your computer
# 3. Update audio drivers
```

### ❌ "Could not request results from Google"
- Check internet connection: `ping google.com`
- Wait a moment and try again
- Ensure Google Speech API is accessible in your region

### ❌ "Assistant doesn't hear me"
1. Speak louder and closer to microphone
2. Reduce background noise
3. Ensure microphone is not muted
4. Check microphone volume level

### ❌ "ImportError: No module named 'speech_recognition'"
```bash
# Reinstall dependencies:
pip install --upgrade -r requirements.txt
```

---

## 📊 Which Version Should I Use?

### 👶 Basic Version (`voice_assistant.py`)
**Best for:**
- Learning how voice assistants work
- Getting started quickly
- Simple tasks (time, date, search, jokes)
- Lower system requirements

**Commands:** 7 main commands

### 🚀 Advanced Version (`voice_assistant_advanced.py`)
**Best for:**
- Complete voice assistant experience
- Weather information
- Setting and checking reminders
- More advanced NLP
- Ready for customization

**Commands:** 15+ commands with parameters

---

## 💡 Pro Tips

1. **Speak Clearly**: Pronounce words clearly for better recognition
2. **One Command at a Time**: Say one command, wait for response
3. **Use Natural Language**: "What time is it?" works better than "time"
4. **Check Console**: Error messages appear in the command prompt
5. **Test Microphone First**: Run `python -m speech_recognition` to test
6. **Low Noise Environment**: Find a quiet space for better recognition

---

## 🔧 System Requirements

- **Python:** 3.7 or higher
- **RAM:** 512 MB minimum
- **Internet:** Required (for Google Speech API)
- **Microphone:** Any USB or built-in microphone
- **OS:** Windows, Mac, or Linux

---

## 📱 Testing the Assistant

### Test 1: Basic Response
```bash
python voice_assistant.py
YOU: "Hello"
EXPECTED: "Good morning/afternoon/evening!"
```

### Test 2: Time Query
```
YOU: "What time is it?"
EXPECTED: Current time spoken aloud
```

### Test 3: Search Function
```
YOU: "Search for weather"
EXPECTED: Browser opens Google search for "weather"
```

### Test 4: Error Handling (Advanced)
```
YOU: [Stay silent]
EXPECTED: "I didn't hear anything. Please try again."
```

---

## 🎯 Next Steps After Setup

1. **Customize Commands**: Edit the process_command() function
2. **Add More Jokes**: Add entries to the jokes list
3. **Integrate APIs**: Add weather, email, or calendar APIs
4. **Create a GUI**: Build a graphical interface
5. **Deploy**: Run as a background service or in cloud

---

## 📞 Need Help?

1. **Check Console Error**: Read the error message carefully
2. **Review README.md**: Detailed documentation
3. **Check Microphone Settings**: System audio settings
4. **Test Each Component**: Run test scripts
5. **Update Libraries**: `pip install --upgrade -r requirements.txt`

---

## ✅ Verification Checklist

Before reporting issues:
- [ ] Python 3.7+ installed: `python --version`
- [ ] All packages installed: `pip list | grep -E 'speech_recognition|pyttsx3|requests'`
- [ ] Microphone connected and working
- [ ] Internet connection active
- [ ] Running as normal user (not root)
- [ ] No other app using microphone
- [ ] Console shows no Python errors

---

## 🎉 Success!

If your assistant responds with "Voice Assistant started" and "How can I help you?" - **You're all set!**

Start giving commands and enjoy your Voice Assistant! 🎤🤖

---

**Last Updated:** June 2026
**Version:** 2.0
**Status:** Ready to Use ✅
