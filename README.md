# Setup Guide

## Prerequisites

Before running the project, make sure you have Mistral installed on your system and Python 3 available.

## 1. Install Mistral

Install Ollama on your system, then pull the Mistral model:
(For Linux user)
```bash
sudo snap install ollama
```

```bash
ollama pull mistral
```

Start Ollama if it is not already running:

```bash
ollama serve
```

## 2. Clone the Repo
```bash
https://github.com/RuthlessG-CYBER/AI_Agents.git
```

## 3. Create and Activate a Virtual Environment

Create the virtual environment:

```bash
python -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

## 4. Install Required Packages

Install the required Python packages:

```bash
pip install langchain langchain-community langchain-ollama
```

## 5. Run the File

After setup, run your Python file:

```bash
python app.py
```
