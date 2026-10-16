from google import genai
import os
import time

print("Starting ULTRON speed test...")

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY was not found.")
    input("Press Enter to exit...")
    raise SystemExit

client = genai.Client(api_key=api_key)

print("Sending request...")

start = time.perf_counter()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Reply with exactly: ULTRON ONLINE"
)

elapsed = time.perf_counter() - start

print()
print("Gemini replied:")
print(response.text)

print()
print(f"Response time: {elapsed:.2f} seconds")