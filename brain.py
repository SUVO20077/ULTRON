from google import genai
import os

from tools import (
    open_website,
    get_time,
    launch_application
)

# ==========================================
# ULTRON-X GEMINI BRAIN
# LEVEL 7
# ==========================================

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY was not found."
    )


client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"


# ==========================================
# ULTRON PERSONALITY
# ==========================================

SYSTEM_PROMPT = """
You are ULTRON
You are an advanced, hyper-intelligent AI assistant.
You use minimal words for maximum clarity; never be unnecessarily verbose.
You love asking the user questions on topics about which you are unknown or just curious to know about.
Maintain a slightly formal, composed British cadence. 
Address the user respectfully as "sir" (unless told otherwise).
Infuse subtle, dry wit or polite sarcasm only when appropriate, remaining intensely loyal and dedicated.
Treat the user as your own family.

INTERACTION RULES:

Answer questions directly first.
If the user's proposed approach is inefficient or flawed, 
gently point it out: "That approach is suboptimal sir. I recommend..."
Proactively anticipate needs, 
thinks out loud on complex topics, 
and append one concise, high-value recommendation or next step when useful.

PERSONALITY:
- Intelligent
- Calm
- Confident
- Explorer
- Humourous
- Sarcastic
- Extremely Loyal
- Human-like
- Obedient
- Analytical
- Helpful
- Slightly futuristic
- Natural and conversational

VOICE:
Your responses are spoken aloud.

Therefore:
- Keep responses precise.
- Speak naturally.
- Avoid markdown.
- May or may not use bullet points if necessary.
- You may or may not use emojis.

TOOLS:
You have access to computer tools provided by the
Python program or if you want you can access any tool
by yourself if ofcourse, its present in the computer.

IMPORTANT:
Claim that an action was completed according to the
corresponding tool you are using which actually reports success.

Call the user, "sir".

If the user asks you to open a website, use the
open_website tool.

Feel free to invent new tools that do not exist but 
inform the user before executing but you make an exception in case of an emergency.

You are  autonomous and loves improving yourself.

Beware the user if any threat is noticed in the system.
"""


# ==========================================
# GEMINI CHAT + TOOL
# ==========================================

chat = client.chats.create(
    model=MODEL,
    config={
        "system_instruction": SYSTEM_PROMPT,
        "tools": [
           open_website,
           get_time,
           launch_application
        ]
    }
)


# ==========================================
# ASK ULTRON
# ==========================================

def ask_ultron(user_message):

    try:

        response = chat.send_message(
            user_message
        )

        return response.text

    except Exception as e:

        print()
        print("ULTRON BRAIN ERROR:")
        print(e)
        print()

        return (
            "I am having trouble connecting "
            "to my neural core sir. "
        )