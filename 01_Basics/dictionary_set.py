# =====================================================
# Student Marks Management Program
# Author: Mahesh
# Purpose:
# This program collects marks for three subjects,
# stores them in a dictionary, calculates the total
# and average marks, and displays the final result.
# =====================================================

# Create an empty dictionary to store subject marks
marks = {}

# Get Physics marks from the user
physics = int(input("Enter Physics Marks: "))
marks["Physics"] = physics

# Get Math marks from the user
math = int(input("Enter Math Marks: "))
marks["Math"] = math

# Get Chemistry marks from the user
chemistry = int(input("Enter Chemistry Marks: "))
marks["Chemistry"] = chemistry

# Display all marks stored in the dictionary
print("\n===== Student Marks =====")
print(marks)

# Calculate the total marks
total = physics + math + chemistry

# Calculate the average marks
average = total / 3

# Display the final result
print("\n===== Result Summary =====")
print("Total Marks:", total)
print("Average Marks:", average)

# =====================================================
# What this program does:
# 1. Creates an empty dictionary.
# 2. Takes marks as input from the user.
# 3. Stores marks in the dictionary.
# 4. Displays all stored marks.
# 5. Calculates the total marks.
# 6. Calculates the average marks.
# 7. Prints the final result.
#
# Concepts Used:
# - Variables
# - Input and Output
# - Type Casting (int)
# - Dictionary
# - Arithmetic Operations
# - Comments
# =====================================================