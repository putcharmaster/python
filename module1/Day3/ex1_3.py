num_lst = [0,1,2,3]
print(num_lst)
num_lst.extend([2,7,3,3])
print(num_lst)
print("******************************")

lst = [1,3]
lst.extend([7,7,7])
lst.insert(0,100)
lst.insert(0,42)
print(lst)

lst.remove(100)
print(lst)
print("print what's inside in 0th position:",lst[0])
print("print the where \"7\" is",lst.index(7),".position")

ls = ["sam", "tim", "bruno", "federico", "chaya"]
print(ls.index("tim"))
print(ls[0])
print(ls[-1])