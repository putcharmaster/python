list = [1, 5, 3, -42]

print(list)
# print(range(list)) #type list object cannot be interpreted as an int
print(range(len(list)))

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] < list[i + 1]:
            return True
        else:
            return False

def b_sort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break

b_sort(list)               
print(list)

# don't forget len(list) - 1.   "-1"!!!