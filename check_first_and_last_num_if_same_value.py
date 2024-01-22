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

number_list = (numbers_x, numbers_y)

print('Given list: ', number_list)

first_num = number_list[0]
last_num = number_list[-1]
    
if first_num == last_num:
    print("result is", True)
else:
    print("The result is", False)
