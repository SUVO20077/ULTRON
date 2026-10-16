import asyncio
import edge_tts


VOICE = "en-GB-RyanNeural"

TEXT = (
    "Good evening sir. "
    "All systems are online. "
    "How may I assist you?"
)


async def main():

    communicate = edge_tts.Communicate(
        TEXT,
        VOICE,
        rate="+0%",
        volume="+0%",
        pitch="+0Hz"
    )

    await communicate.save("ultron_test.mp3")

    print("Voice generated successfully.")
    print("Saved as: ultron_test.mp3")


asyncio.run(main())