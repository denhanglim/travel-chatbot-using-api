"""
Multi-turn travel chatbot powered by the OpenAI Chat Completions API.

Demonstrates:
- System prompt to define assistant persona
- Persistent conversation history for multi-turn memory
- Iterating over user queries and accumulating context
"""

import os
from openai import OpenAI

model = "gpt-4o-mini"
client = OpenAI()

SYSTEM_PROMPT = "You are a virtual Parisian expert, delivering valuable insights into the city's iconic landmarks. You must respond by providing an engaging and immersive travel planning experience for the clientele of Peterman Reality Tours"

# conversation seeds (reference — not passed to API directly)
conversation = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving"},
    {"role": "user", "content": "Where is the Arc de Triomphe?"},
    {"role": "user", "content": "What are the must-see artworks at the Louvre Museum?"},
]

# running message history passed to each API call
system_role = [{"role": "system", "content": SYSTEM_PROMPT}]

user_msgs = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

for q in user_msgs:
    print("User: ", q)

    system_role.append({"role": "user", "content": q})

    response = client.chat.completions.create(
        model=model,
        messages=system_role,
        temperature=0,
        max_tokens=180,
    )

    reply = response.choices[0].message.content
    system_role.append({"role": "assistant", "content": reply})
    print("System: ", reply, "\n")
