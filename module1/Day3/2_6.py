password = "password123"

for i in range(3):
    usr_input = input(f"Enter the password ({3-i} attempts remainung)\n")
    if (usr_input == password):
        # print("Password correct!")
        break
    elif(i < 2):
        print("Incorrect. password. Try again") 
if (usr_input == password):
    print("Password correct!")
else:
    print("Incorrect password. No more attempts remaining")