
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

dict = {
    "name" : name,
    "age" : age,
    "city" : city
    
}


print("The content of the dictionary is : ", dict)

print(dict.keys())
print(dict.values())
print(dict.items())