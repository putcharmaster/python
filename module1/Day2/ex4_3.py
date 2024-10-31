import random

random_number = random.randint(1, 100)
print(random_number)
user_input = int(input("Guess the number (1-100):"))

while(user_input != random_number):
    if not (1 <= user_input <= 100):
        print("Choose the number between 0 and 100")
    else:
        if (user_input < random_number):
            print("Too low. Try again")
        elif (user_input > random_number):
            print("Too high. Try again")
    user_input = int(input("Guess the number (1-100):"))

print("Congratulations! You guessed the number!")
            