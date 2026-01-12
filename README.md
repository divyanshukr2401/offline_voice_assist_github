🎙️ Voice Assistance System (Python)

A modular, offline-capable Python-based Voice Assistant built with a clean Listener → Parser → Dispatcher architecture.
This project focuses on real-world speech recognition, system-level command execution, and maintainable software design.

🚧 Status: Actively under development

📌 Project Overview

This voice assistant listens to spoken commands, converts them into text, interprets user intent, and executes corresponding actions such as opening applications or activating specific modes (e.g., coding mode).

The project is designed with:

Scalability in mind

Clear separation of responsibilities

Real-world dependency handling

🧠 Core Architecture (Workflow)

The assistant follows a three-stage pipeline:

1️⃣ Listener

Continuously listens to microphone input

Captures raw audio data

Feeds audio to the speech recognition engine

2️⃣ Parser

Processes recognized text

Extracts intent and relevant keywords

Normalizes and prepares commands for execution

3️⃣ Dispatcher

Maps parsed commands to actions

Calls appropriate modules (OS control, modes, utilities, etc.)

Keeps execution logic decoupled from recognition logic

This architecture ensures:

Easy feature addition

Cleaner debugging

Strong maintainability

🛠️ Technologies & Libraries Used
🔹 Core Technologies

Python

Object-Oriented Programming (OOP)

Virtual Environments

🔹 Speech Recognition

Vosk (offline, lightweight, reliable)

🔹 Audio Handling

PyAudio

Note: Python version had to be downgraded to ensure PyAudio compatibility.

🔹 System Interaction

os

subprocess

Platform-specific OS handling

❓ Why Vosk Instead of Faster-Whisper?

I initially planned to use Faster-Whisper, but:

Installation required heavy dependencies

Platform and environment compatibility issues occurred

Resource usage was higher than needed for this project

Vosk was chosen because:

Works fully offline

Easier to integrate

Lightweight and stable for real-time command recognition


Create & activate virtual environment

  >> python -m venv venv

  >> source venv/bin/activate  # Linux / macOS

  >> venv\Scripts\activate


🚀 Current Features

Offline speech recognition

Modular command handling

Voice-triggered application control

Mode-based execution logic

Clean OOP-based architecture
