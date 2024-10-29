amount = int(input("How many tickets do you need: "))
student = input("Do you have student discount (y/n)? ")

if student == "y":
    ticket = 10 * amount
elif student == "n":
    ticket = 15 * amount
else:
    print("Incorrect input.")
    exit()
    
print("Total tickets price :",ticket,"euros")