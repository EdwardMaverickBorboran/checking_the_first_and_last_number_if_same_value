# Create a program that will --

# Return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Given
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Expected Output:
# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

# First list of given numbers
print('Given list:', numbers_x)

first_num = numbers_x[0]
last_num = numbers_x[-1]
    
if first_num == last_num:
    print("The result is", True)
else:
    print("The result is", False)

# Second list of given numbers
print('Given list:', numbers_y)

first_num = numbers_y[0]
last_num = numbers_y[-1]
    
if first_num == last_num:
    print("The result is", True)
else:
    print("The result is", False)