# Travel Chatbot Using API

A multi-turn travel chatbot powered by the OpenAI Chat Completions API. Acts as a virtual Parisian expert for Peterman Reality Tours, answering a series of travel questions while maintaining full conversation history across turns.

## What it demonstrates

- **System prompts** — defining an assistant persona
- **Multi-turn memory** — appending each question and answer to `messages` so the model has full context on every call
- **Chat Completions API** — structured `messages` list with `user` / `assistant` / `system` roles

## Sample output

```
User:  How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?
System:  Ah, what a wonderful question! The Louvre Museum and the Eiffel Tower are both iconic
landmarks in the heart of Paris...

User:  Where is the Arc de Triomphe?
System:  The Arc de Triomphe stands majestically at the western end of the Champs-Élysées...
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/travel-chatbot-using-api.git
cd travel-chatbot-using-api
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your OpenAI API key**
```bash
cp .env.example .env
# open .env and replace "your-key-here" with your actual key
```

**4. Run**
```bash
python Travel_Chatbot_Using_API.py
```

## Requirements

- Python 3.8+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
