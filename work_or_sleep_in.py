while True:
    day = int(input('Day (0-6)? '))
    if day >= 1 and day < 6:
        print ("Go to work")
        break
    elif day == 0 or day == 6:
        print ("Sleep in")
        break
    else:       #verify number is valid
        print ("Please enter a number between 0-6")
