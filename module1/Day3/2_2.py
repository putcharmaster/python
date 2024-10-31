lst = [1,0,111,31,42,22, 3,7,3,8]
print("original lst: ", lst)
lst.sort()

even_nr = []

for i in lst:
    if i % 2 == 0:
        even_nr.append(i)
    
print("this is the list: ", lst)
print("even number from the list: ", even_nr)