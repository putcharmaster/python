

def pyramid(levels):
    for i in range(levels):
        print(' ' * (levels - i -1), end='')
        print('*' * (2 * i + 1))
levels = int(input("Enter the number of levels for the pyramid: "))
pyramid(levels)





# try:
#     levels = int(input("Enter the number of levels for the pyramid: "))
#     pyramid(levels)
# except ValueError:
#     print("Please enter a valid integer.")
