import speech_recognition as sr
import pyttsx3
import time
from datetime import datetime


# ==========================================
# ULTRON VOICE CORE
# LEVEL 6.2
# ==========================================

recognizer = sr.Recognizer()


# ==========================================
# SPEAK
# ==========================================

def speak(text):

    print(f"ULTRON: {text}")

    # Create a fresh Windows TTS engine
    engine = pyttsx3.init("sapi5")

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()

# ==========================================
# LISTEN
# ==========================================

def listen():

    with sr.Microphone() as source:

        print()
        print("🎤 Listening...")

        # Small adjustment for room noise
        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            return ""

    try:

        text = recognizer.recognize_google(
            audio
        )

        print(f"YOU: {text}")

        return text.lower()

    except sr.UnknownValueError:

        print("ULTRON: I couldn't understand that.")

        return ""

    except sr.RequestError:

        speak(
            "I am unable to reach the speech "
            "recognition service."
        )

        return ""


# ==========================================
# COMMAND PROCESSOR
# ==========================================

def process_command(command):

    if not command:
        return True

    # --------------------------------------
    # GREETING
    # --------------------------------------

    if (
        "hello ultron" in command
        or "hi ultron" in command
        or "hey ultron" in command
    ):

        speak(
            "Hello. Systems are online. "
            "How may I assist you?"
        )

    # --------------------------------------
    # HOW ARE YOU
    # --------------------------------------

    elif "how r u" in command:

        speak(
            "All systems are functioning "
            "within normal parameters."
        )

    # --------------------------------------
    # WHO ARE YOU
    # --------------------------------------

    elif (
        "who are you" in command
        or "what are you" in command
    ):

        speak(
            "I am Ultron. Your personal "
            "computer assistant."
        )

    # --------------------------------------
    # TIME
    # --------------------------------------

    elif "time" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is "
            f"{current_time}."
        )

    # --------------------------------------
    # DATE
    # --------------------------------------

    elif "date" in command:

        current_date = datetime.now().strftime(
            "%A, %d %B %Y"
        )

        speak(
            f"Today is {current_date}."
        )

    # --------------------------------------
    # SHUTDOWN
    # --------------------------------------

    elif (
        "shutdown ultron" in command
        or "stop ultron" in command
        or "goodbye ultron" in command
    ):

        speak(
            "Understood. Shutting down "
            "voice systems."
        )

        return False

    # --------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------

    else:

        speak(
            "I heard you, but I do not "
            "know how to perform that "
            "command yet."
        )

    return True


# ==========================================
# START ULTRON
# ==========================================

print()
print("==========================================")
print("             ULTRON-X")
print("          VOICE SYSTEM ONLINE")
print("==========================================")
print()

speak(
    "Voice systems online. "
    "I am ready."
)


# ==========================================
# MAIN CONVERSATION LOOP
# ==========================================

running = True

while running:

    command = listen()

    running = process_command(
        command
    )

    time.sleep(0.2)


# ==========================================
# SHUTDOWN
# ==========================================

print()
print("==========================================")
print("       ULTRON VOICE SYSTEM OFFLINE")
print("==========================================")