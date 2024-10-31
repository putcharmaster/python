lst = ["hi", "hi", "did", "you", "hear", "me", "hi"]
print(lst.count("hi"))
print(lst)
lst.reverse()
print(lst)

num_lst = [6,5,1,2,7,9]
print(num_lst)
num_lst.sort()
print(num_lst)
print(num_lst)
print(num_lst[0])
num_lst.reverse()
print(num_lst)

n_lst = [3,7,21,24,42]
print(n_lst)
total = 0
for i in n_lst:
    print(total,"old total")
    print("+")
    total += i
    print(i)
    print("total",total)
    print("%%%%%%%%%%%%%%%%")
print("total:",total)

