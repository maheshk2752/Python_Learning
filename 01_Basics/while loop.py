 
# Program: Display Student Scores
# Author : Ram  Beekhani
# Purpose:
# This program demonstrates the use of a for loop
# to iterate through a list of student scores and
# display each score with its position.
# =====================================================

# List of student scores
student_scores = [85, 92, 78, 96, 88]

# Display heading
print("Student Score Report")
print("-" * 25)

# Iterate through the list using a for loop
for index, score in enumerate(student_scores, start=1):
    print(f"Student {index}: {score} marks")

# Display completion message
print("-" * 25)
print("Report Generated Successfully!")