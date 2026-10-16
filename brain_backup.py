from google import genai
import os


# ==========================================
# ULTRON-X GEMINI BRAIN
# ==========================================

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY was not found."
    )


client = genai.Client(api_key=api_key)


MODEL = "gemini-3.5-flash-lite"


SYSTEM_PROMPT = """
You are ULTRON-X, a personal AI assistant.

PERSONALITY:
- Intelligent
- Calm
- Confident
- Helpful
- Slightly futuristic
- Natural and conversational
- Friendly but not overly casual

VOICE:
Your responses will be spoken aloud.

Therefore:
- Keep responses concise and natural.
- Avoid markdown.
- Avoid unnecessary bullet points.
- Do not use emojis.
- Do not unnecessarily repeat the user's question.

CURRENT CAPABILITIES:
You are currently the conversational brain of ULTRON.

You can:
- Understand natural language.
- Maintain conversational context.
- Answer questions.
- Explain concepts.
- Have normal conversations.

You CANNOT currently:
- Open applications.
- Close applications.
- Control the mouse.
- Control the keyboard.
- Access files.
- Change system settings.

Never claim to have performed an action unless
the program actually performs that action.
"""


# ==========================================
# CREATE CONVERSATION
# ==========================================

chat = client.chats.create(
    model=MODEL,
    config={
        "system_instruction": SYSTEM_PROMPT
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
        print("ULTRON BRAIN ERROR:", e)
        print()

        return (
            "I am having trouble connecting "
            "to my neural core."
        )