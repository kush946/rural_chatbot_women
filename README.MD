# Rural Women Welfare Voice Assistant (Telangana)

An offline conversational AI assistant that helps rural women discover eligible government schemes using Telugu speech or text.

## Features

* Telugu speech recognition (offline Vosk)
* Handles spoken Telugu & Tanglish
* Asks intelligent follow-up questions
* Suggests top eligible welfare schemes
* Shows documents, benefits, application process
* Domestic violence emergency helpline support
* Works without internet

---

## How It Works

User speaks → system understands intent → collects missing details → checks eligibility → recommends schemes.

---

## Installation

### 1. Clone repo

git clone https://github.com/yourusername/rural-welfare-voice-assistant.git
cd rural-welfare-voice-assistant

### 2. Create environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Download Vosk Telugu Model

Download from: https://alphacephei.com/vosk/models
Place inside `/models/`

---

## Run Assistant

python app/conversation_main.py

---

## Example Queries

* widow pension kavali
* pregnancy help kavali
* muslim marriage help
* operation ki dabbu kavali
* naa husband nannu kottutunnadu

---

## Target Users

Rural women with low literacy and limited internet access.

---

## Key Contribution

An explainable conversational eligibility engine instead of a static chatbot.
