from google.cloud import texttospeech


client = texttospeech.TextToSpeechClient()


text = "Good evening, sir. Neural voice systems are now online."


synthesis_input = texttospeech.SynthesisInput(
    text=text
)


voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB",
    name="en-GB-Neural2-D"
)


audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)


response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)


with open("ultron_test.mp3", "wb") as audio_file:
    audio_file.write(response.audio_content)


print("ULTRON voice generated successfully.")
print("Saved as ultron_test.mp3")