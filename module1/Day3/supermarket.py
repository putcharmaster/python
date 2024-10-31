answer = input("Would you like to\n (1) input a new product,\n (2) see the list of products, or\n (3) exit?\n")
lst = {}

while answer != "3":
    if answer == "1":
        code = int(input("Code of the product: "))
        name = input("Name of the product: ")
        lst[code] = name
    elif answer == "2":
        for x, y in lst.items():
            print(x, "-", y)
    else:
        print("Invalid answer")
    
    answer = input("Would you like to\n (1) input a new product,\n (2) see the list of products, or\n (3) exit?\n")
    
print("Good bye!")

#########unfinished#########################################