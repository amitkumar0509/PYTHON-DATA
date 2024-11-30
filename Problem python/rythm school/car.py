command = input("Enter 'start' to begin or 'stop' to stop: ").lower()

while command == "start" or command == "stop":
    if command == "start":
        print("The car starts")
    elif command == "stop":
        print("The car stops")
    command = input("Enter 'start' to begin or 'stop' to stop (or anything else to exit): ").lower()

print("Sorry, I don't understand that command")
