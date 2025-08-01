# Voice-Controlled WhatsApp Chatbot

This is a voice-activated chatbot that can open WhatsApp Web, search for a contact, read recent messages, and reply using GPT‑4.1 It’s built using Python, OpenAI’s API, and speech recognition.

## Features

-  Listens for voice command like **"Reply"**
-  Searches and opens the specified contact on WhatsApp Web
-  Uses GPT-4.1 to read the latest messages and generate smart replies
-  Easy to set up with virtual environment and requirements.txt

##  Requirements

- Python 3.8+
- OpenAI API key
- Google Chrome + WhatsApp Web
- Microphone

##  Installation

```bash
# Clone the repository
git clone https://github.com/Preet-Shah04/Chatbot-Voice-assist-.git
cd Chatbot-Voice-assist-

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate         # On Windows
source .venv/bin/activate      # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python main.py

Speak the command: "Reply"

The bot will:
Open WhatsApp Web

Search for the contact you specify in the code (currently hardcoded)
Read the last messages
Use GPT‑4.1 to generate and send a reply


##  Configuration
Update the following in your code:

Set your OpenAI API key securely:
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
You can create a .env file (optional) or set environment variables.

##  Files Included
File                          Description  
------------------------------------------------------------	             
main.py	             Main logic for listening and replying
position.py	         Defines the pixel positions for automation
requirements.txt	 Required Python libraries
.gitignore	         Hides virtual environment & sensitive files


## 🛡️ Notes
Make sure WhatsApp Web is logged in
Works best on 1920×1080 screen resolution
You can customize the contact name inside the main.py file

## 🙋‍♂️ Author
Developed by Preet Shah
[LinkedIn Profile](https://www.linkedin.com/in/preet-shah-a10b3b32b/)
Email: preetshah0407@mail.com
