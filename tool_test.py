from brain import ask_ultron


print()
print("==========================================")
print("       ULTRON-X LEVEL 7 TOOL TEST")
print("==========================================")
print()


while True:

    command = input("YOU: ")

    if command.lower() in [
        "exit",
        "quit",
        "shutdown"
    ]:

        print("ULTRON: Shutting down.")
        break


    response = ask_ultron(command)

    print()
    print("ULTRON:", response)
    print()