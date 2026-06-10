# Create a list of numbers
my_list = [1, 2, 1]

# Create a copy of the original list
copy_list = my_list.copy()

new_list =[3,4,5,6]

# Reverse the copied list
copy_list.reverse()

# Compare the original list with the reversed list
if copy_list == new_list:
    # If both lists are the same, it is a palindrome
    print("Palindrome")
else:
    # If the lists are different, it is not a palindrome
    print("Not Palindrome")