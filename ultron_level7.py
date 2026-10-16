import speech_recognition as sr
import pyttsx3

from brain import ask_ultron


# ==========================================
# ULTRON-X
# LEVEL 7 — VOICE + GEMINI + TOOLS
# ==========================================

recognizer = sr.Recognizer()


# ==========================================
# SPEAK
# ==========================================

def speak(text):

    print()
    print(f"ULTRON: {text}")
    print()

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

        try:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
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

        print(
            "ULTRON: I couldn't understand that."
        )

        return ""

    except sr.RequestError:

        speak(
            "My speech recognition service "
            "is currently unavailable."
        )

        return ""


# ==========================================
# START ULTRON
# ==========================================

print()
print("==========================================")
print("             ULTRON-X")
print("        LEVEL 7 ONLINE")
print("==========================================")
print()
print("🧠 Gemini Neural Core: ONLINE")
print("🎤 Voice Recognition: ONLINE")
print("🔊 Voice Synthesis: ONLINE")
print("🌐 Website Tool: ONLINE")
print("🕒 Time Tool: ONLINE")
print()

speak(
    "Neural core online. "
    "All primary systems are operational."
)


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    command = listen()

    if not command:
        continue


    # --------------------------------------
    # SHUTDOWN
    # --------------------------------------

    if (
        "shutdown ultron" in command
        or "stop ultron" in command
        or "goodbye ultron" in command
    ):

        speak(
            "Understood. "
            "Shutting down all voice systems."
        )

        break


    # --------------------------------------
    # GEMINI
    # --------------------------------------

    response = ask_ultron(command)


    # --------------------------------------
    # SPEAK RESPONSE
    # --------------------------------------

    speak(response)


print()
print("==========================================")
print("             ULTRON OFFLINE")
print("==========================================")