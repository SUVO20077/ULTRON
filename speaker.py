import asyncio
import os
import tempfile

import edge_tts
import pygame


VOICE = "en-GB-RyanNeural"


# Initialize audio system once
pygame.mixer.init()


def speak(text):

    print()
    print(f"ULTRON: {text}")
    print()

    temp_file = None

    try:
        # Create temporary MP3 file
        with tempfile.NamedTemporaryFile(
            suffix=".mp3",
            delete=False
        ) as file:

            temp_file = file.name

        # Generate speech
        async def generate():

            communicate = edge_tts.Communicate(
                text,
                VOICE,
                rate="+0%",
                volume="+0%",
                pitch="+0Hz"
            )

            await communicate.save(temp_file)

        asyncio.run(generate())

        # Stop anything currently playing
        pygame.mixer.music.stop()

        # Load generated speech
        pygame.mixer.music.load(temp_file)

        # Play
        pygame.mixer.music.play()

        # Wait until finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(20)

    except Exception as e:

        print()
        print("ULTRON TTS ERROR:")
        print(e)
        print()

    finally:

        pygame.mixer.music.stop()

        if temp_file and os.path.exists(temp_file):

            try:
                os.remove(temp_file)

            except PermissionError:
                pass