import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import speech_recognition as sr
from voice.speaker import speak

from brain import ask_ultron

from core.state import UltronState
from voice.voice_controller import process_voice_command
from voice.speaker import speak
state = UltronState()

# ==========================================
# ULTRON-X
# LEVEL 7.5
# VOICE + GEMINI + TOOLS
# ==========================================

recognizer = sr.Recognizer()

recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.5
recognizer.phrase_threshold = 0.3


# ==========================================
# LISTEN
# ==========================================

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=15
            )

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

    try:

        text = recognizer.recognize_google(
            audio
        )

        print(f"YOU: {text}")

        return text

    except sr.UnknownValueError:

        print("ULTRON: I couldn't understand that sir.")
        return ""

    except sr.RequestError:

        speak(
            "My speech recognition service "
            "is currently unavailable sir."
        )

        return ""

# ==========================================
# MICROPHONE CALIBRATION
# ==========================================

print("🎧 Calibrating microphone...")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(
        source,
        duration=1
    )

print("🎤 Microphone ready.")


# ==========================================
# ULTRON STARTUP
# ==========================================

print()
print("==========================================")
print("              ULTRON-X")
print("             LEVEL 7.5")
print("==========================================")
print()
print("🧠 Gemini Neural Core : ONLINE")
print("🎤 Voice Recognition  : ONLINE")
print("🔊 Voice Synthesis    : ONLINE")
print("🌐 Website Tool       : ONLINE")
print("🕒 Time Tool          : ONLINE")
print("🖥️ Application Tools  : ONLINE")
print()

speak(
    "Neural core online. "
    "Voice command systems are ready. "
    "Hello sir."
)


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    command = listen()

    if not command:
        continue

    command_lower = command.lower().strip()

    # ==================================
    # SHUTDOWN
    # ==================================

    if command_lower in [
        "shutdown",
        "stop",
        "goodbye"
    ]:
        speak("Goodbye sir.")
        state.ultron_active = False
        break


    # ==================================
    # LOCAL COMMAND ROUTER
    # ==================================

    local_response = process_voice_command(
        command,
        state
    )

    if local_response is not None:

        speak(local_response)

        continue


    # ==================================
    # GEMINI
    # ==================================

    response = ask_ultron(command)

    speak(response)


print()
print("==========================================")
print("            ULTRON OFFLINE")
print("==========================================")