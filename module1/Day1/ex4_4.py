# 4.4 - Strings Search for words in Strings
# Instructions The owner of a restaurant is interested in whether clients like their 
# specialties: chocolate cake and barbecue.
# Write a program that asks the user for the dishes they like and prints 
# the search result:
# - If the dish is found, the program prints the number of the symbol from 
# which the dish begins.
# - If the dish is not found, the program prints -1.
# Take into account that the client’s review might include uppercase and 
# lowercase letters.
# Expected output Enter your favorite dishes:
# >>>barbecue, burger, pizza
# chocolate cake: -1
# barbecue: 0

dishes = input("Enter your favorite dishes: ").split(", ")
print(dishes)

search_terms = ["chocolate cake", "barbecue"]
for term in search_terms:
	index = -1
	for dish in dishes:
		if term.lower() in dish.lower():
			index = dishes.index(dish)
			break
	print(f"{term}: {index}")