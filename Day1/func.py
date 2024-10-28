def callme():
    print("did you call me")
callme()

def add(a, b):
    return a + b
    
a,b = 1, 2
print(a,b)
c = add(a,b)
print(c)

n1 = 3
n2 = 10
n3 = 11
print(n1, n2, n3)
n1, n2 = n2, n1
print(n1, n2, n3)

n1, n2, n3 = n2, n3, n1
print(n1, n2, n3)

s1 = "hello"
s2 = 'world'
s3 = "python "
concat = s1+" "+s2
rep = s3*3
print("str concat :", concat)
print("rep : ", rep)