age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

if 18 <= age <= 25 and 3.0 <= gpa <= 7.0:
    print("Congratulations! You're eligible for admission.")
elif 18 <= age <= 25 or 3.0 <= gpa <= 7.0:
    print("You don't meet all the requirements.")
else:
    print("Sorry, You're not eligible for admission.")