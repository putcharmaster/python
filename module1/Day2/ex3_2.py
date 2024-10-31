# p = [0] * 4 # Initialize the list with 4 elements

# for i in range(1, 4):
#     p[i] = int(input(f"Price of product {i}: "))
    
# for i in range(1, 4):
#     print(f"p{i} = {p[i]}")

p1 = int(input("Price of product 1: "))
p2 = int(input("Price of product 2: "))
p3 = int(input("Price of product 3: "))
    
if (p1 > p2):
    if (p1 > p3):
        print("Promotion! Total for three items: ", p1)
    else:
        print("Promotion! Total for three items: ", p2)
else:
    if (p2 > p3):
        print("Promotion! Total for three items: ", p2)
    else:
        print("Promotion! Total for three items: ", p3)
        
        
        
        