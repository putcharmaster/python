user_input = input("Enter the password: ")

while (user_input != "password123"):
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")
    
print("Password correct!")