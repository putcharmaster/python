# print((10/2) + (5 // 2))

result1 = 5 + 3 * 2
result2 = (5 + 3) * 2
result3 = 8 / 2 * 4
result4 = 8 * 4 / 2
result5 = 5 + 2 ** 3
result6 = (5 + 2) ** 3
result7 = 10 % 3 + 2 * 3
result8 = 10 % (3 + 2) * 3
result9 = 10 / 2 + 5 // 2
result10 = (10 / 2) + (5 // 2)

for i in range(1, 11):
    print(globals()[f'result{i}'])
    print(f"result of {i} is: {globals()[f'result{i}']}")
    