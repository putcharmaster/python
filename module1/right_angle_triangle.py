# rows = int(input("Number of rows :"))

# for i in range(rows):
#     print(i+1)

def number_triangle(rows):
    for i in range(1, rows + 1):
        # print(" ".join(str(num) for num in range(1, i + 1)))
        for num in range(1, i + 1):
            print(num, end=" ") 
        print() 
        
rows = int(input("Enter the number of rows for the right-angle triangle: "))
number_triangle(rows)
                

# # Get the number of rows from the user
# try:
#     rows = int(input("Enter the number of rows for the right-angle triangle: "))
#     number_triangle(rows)
# except ValueError:
#     print("Re-run the program. Please enter a valid integer.")
