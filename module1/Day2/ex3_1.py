answer = input("Would you like promotional items (yes/no)? ")


if answer == "no":
    print("Let us know if you change your mind!")
    exit()
elif answer == "yes":
    cat = input("Enter a category: ")
    if cat == "sweets":
        print("Gummy fruit for 200 coins")
    else:
        print("Lingonberry juice for 140 coins")
else:
    print("wrong input")
    exit()