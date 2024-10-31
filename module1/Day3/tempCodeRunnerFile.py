if answer == 1:
        code = int(input("Code of the product: "))
        name = input("Name of the product: ")
        lst[code] = name
    elif answer == 2:
        for x, y in lst.items():
            print(x, "-", y)