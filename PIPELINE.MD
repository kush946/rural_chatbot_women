# System Pipeline Documentation

## Overview

The assistant follows a multi-stage decision pipeline rather than a simple chatbot response.

---

## 1. Input Layer

Input Modes:

* Telugu voice
* Tanglish typed text

Voice → converted to text using Vosk offline speech recognition.

---

## 2. Intent Detection

The system identifies the user's problem category:

* marriage_support
* pregnancy_support
* pension_support
* health_support
* employment_support
* violence_support

Uses fuzzy matching for spelling mistakes.

---

## 3. Attribute Extraction

Extracts structured user information:

* age
* income level
* religion
* widow/divorced status
* pregnancy
* illness
* skills

Handles Telugu number words.

---

## 4. Adaptive Question Engine

If data is missing:
System asks most relevant next question.

Instead of fixed forms:
Dynamic questioning based on eligibility requirements.

---

## 5. Eligibility Ranking Engine

Each scheme scored using:

* match conditions
* partial match

- conflicting conditions

Top 3 schemes returned.

---

## 6. Explanation Layer

Shows:

* Benefits
* Documents
* Application steps
* Notes

Displayed in Telugu.

---

## 7. Safety Layer

If domestic violence detected:
System bypasses eligibility engine
Shows emergency helpline immediately.

---

## Key Innovation

Conversational eligibility reasoning system rather than keyword chatbot.
