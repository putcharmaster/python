nr_member = int(input("Number of participants: "))
member = []
for i in range(nr_member):
    name = input("Enter name:")
    member.append(name)
    print(f"Welcome {name}")
print("Group chat created!")
print(member)
    
    