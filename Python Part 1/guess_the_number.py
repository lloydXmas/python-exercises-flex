import random

my_random_number = random.randint(1, 10)
counter = 0
repeat = True

print ("I am thinking of a number between 1 and 10.")
while repeat:
    while counter < 5 and repeat:
        remaining_guesses = 5 - counter
        print ("You have " + str(remaining_guesses) + " guesses left.")
        guessed_num = input("What's the number? ")
        num_check = int(guessed_num)
        if num_check == my_random_number:
            print ("Yes! You win!")
            break
        elif num_check > my_random_number:
            print (guessed_num + " is too high.")
            counter += 1
        elif num_check < my_random_number:
            print (guessed_num + " is too low.")
            counter += 1

    if counter == 5:
        print("You ran out of guesses!")
    go_again = input("Do you want to play again (Y or N)? ")
    go_again = go_again.upper()
    if go_again == "N":
        repeat = False
        print ("Bye")
    else:
        counter = 0
