option = ""
started = False
while True:
    option = input("> ")
    if option == "help":
        print("for start the car write start")
        print( "for stop the car write stop")
        print( "for quit write exit")
    elif option == "start":
        if started:
            print("car alredy started")
        else:
            started = True
            print("car is ON")
    elif option == "stop":
        print("car is OFF")
    elif option == "exit":
        break
    else:
        print("I dont understand")
