amount = float(input("Total bill amount? "))
service = input("Level of service? ")
if service.lower() == "good":
    tip = float(amount * 0.20)
    total = float(tip + amount)
    print ("Tip amount: ${:.2f}".format(tip))
    print ("Total amount: ${:.2f}".format(total))
elif service.lower() == "fair":
    tip = float(amount * 0.15)
    total = float(tip + amount)
    print ("Tip amount: ${:.2f}".format(tip))
    print ("Total amount: ${:.2f}".format(total))
elif service.lower() == "bad":
    tip = float(amount * 0.10)
    total = float(tip + amount)
    print ("Tip amount: ${:.2f}".format(tip))
    print ("Total amount: ${:.2f}".format(total))
