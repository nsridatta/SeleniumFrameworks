command = ""
started = False

while True:
    command = (input(">")).lower()

    if command == "start":
        if started:
            print("Car Already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car Already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start   -   to start the car
stop    -   to stop the car
quit    -   Quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, Not able to understand that!")

