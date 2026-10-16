from brain import ask_ultron


print()
print("==========================================")
print("          ULTRON-X GEMINI BRAIN")
print("==========================================")
print()

while True:

    question = input("YOU: ")

    if question.lower() in [
        "exit",
        "quit",
        "shutdown"
    ]:
        print("ULTRON: Shutting down.")
        break

    try:

        answer = ask_ultron(question)

        print()
        print("ULTRON:", answer)
        print()

    except Exception as e:

        print()
        print("ULTRON BRAIN ERROR:")
        print(e)
        print()