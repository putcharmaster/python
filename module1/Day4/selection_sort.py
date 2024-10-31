list = [9328, 38, 3287, 221, 42, 777]

def sel_sort(list):
    n = len(list)
    for i in range(n):
        min = i
        swapped = False
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j
                swapped = True
            if not swapped:
                break
        if i != min:
            list[i],list[min] = list[min],list[i]
            
sel_sort(list)
print(list)
        
            