num_coins = 0
answer = ""
print ("You have", str(num_coins), "coins.")
while answer != 'no':
    answer = input("Do you want another? ")
    answer = answer.lower()
    if answer == "yes":
        num_coins += 1
    print ("You have ", str(num_coins), "coins.")

print("Bye")
