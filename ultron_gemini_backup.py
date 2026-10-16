import speech_recognition as sr
import pyttsx3

from brain import ask_ultron


# ==========================================
# ULTRON-X VOICE + GEMINI
# LEVEL 6.3
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
# START
# ==========================================

print()
print("==========================================")
print("           ULTRON-X ONLINE")
print("       GEMINI NEURAL CORE ACTIVE")
print("==========================================")
print()

speak(
    "Neural core online. "
    "Voice systems are ready."
)


# ==========================================
# CONVERSATION LOOP
# ==========================================

while True:

    command = listen()

    if not command:
        continue


    # --------------------------------------
    # SHUTDOWN
    # --------------------------------------

    if (
        "shutdown" in command
        or "stop" in command
        or "goodbye" in command
    ):

        speak(
            "Understood. "
            "Goodbye , sir."
        )

        break


    # --------------------------------------
    # SEND TO GEMINI
    # --------------------------------------

    response = ask_ultron(
        command
    )


    # --------------------------------------
    # SPEAK GEMINI RESPONSE
    # --------------------------------------

    speak(response)


print()
print("==========================================")
print("        ULTRON-X OFFLINE")
print("==========================================")