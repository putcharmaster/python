lst = ["applEee", "baAAanaana", "cheEerrrryy", "kiIiiiiwi"]

v_lst = []

for str in lst: #increment lst[str++]
    count = 0
    print("**",str,"**")
    for i in str: #increment str[i++]
        if (i) in "AEIOU":
            count += 1
    v_lst.append(count)
    print(v_lst)
print("vowels list: ", v_lst)