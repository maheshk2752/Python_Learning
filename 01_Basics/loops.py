# =====================================================
# Program: Search a Number in a List using While Loop
# Author: Mahesh
# Purpose:
# This program searches for a specific number in a list
# and displays the index where the number is found.
# =====================================================

# List of square numbers
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Number to search for
x = 36

# Starting index
i = 0

# Loop through the list until the end
while i < len(nums):

    # Check if the current element matches the target number
    if nums[i] == x:
        print("Found at index:", i)
        break  # Stop searching once the number is found

    # If the number is not found at the current index
    else:
        print("Finding...")

    # Move to the next index
    i += 1