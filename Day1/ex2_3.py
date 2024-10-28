# 2.3 - Variables and operations
# Print the total amount allocated
# Instructions
# There is a request for the purchase of computers and components for them:
# - 6 laptops for 55,480 dollars each;
# - 3 monitors for 21,830 dollars each;
# - 11 computer mice for 411 dollars each;
# - 5 keyboards for 290 dollars each.

# Calculate how much to allocate from the company's budget.

# Use 4 variables to store the prices of each of the components.
# Expected output
# Need to allocate: 404341


laptop = 55480
monitor = 21830
mouse = 411
keyboard = 290

total = (laptop * 6)+(monitor*3)+(mouse*11)+(keyboard*5)
print("Need to allocate: ",total)