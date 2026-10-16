import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

print("\nAvailable ULTRON voices:\n")

for i, voice in enumerate(voices):
    print(f"VOICE {i}")
    print("Name:", voice.name)
    print("ID:", voice.id)
    print("-" * 50)

engine.stop()