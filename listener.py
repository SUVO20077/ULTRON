import speech_recognition as sr

recognizer = sr.Recognizer()

print("====================================")
print("        ULTRON VOICE SYSTEM")
print("====================================")
print()
print("🎤 Listening...")
print("Speak something!")
print()

with sr.Microphone() as source:

    recognizer.adjust_for_ambient_noise(
        source,
        duration=1
    )

    print("ULTRON: I am listening.")

    audio = recognizer.listen(source)

try:

    text = recognizer.recognize_google(audio)

    print()
    print("YOU:", text)

except sr.UnknownValueError:

    print()
    print("ULTRON: I couldn't understand that.")

except sr.RequestError as e:

    print()
    print("ULTRON: Speech recognition service unavailable.")
    print("ERROR:", e)