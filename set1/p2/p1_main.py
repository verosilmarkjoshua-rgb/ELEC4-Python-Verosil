# Name: MARK JOSHUA VEROSIL
# Section: IV-BSIT A
# Activity: P2 - Main program using student_utils
# Date: November 27, 2026

import student_utils                          # style 1: import the whole module
from student_utils import get_status          # style 2: import one name only
from datetime import datetime                 # built-in module

grades = []
total_subjects = int(input("How many grades? "))

for subject_no in range(total_subjects):
    score = float(input("Grade " + str(subject_no + 1) + ": "))
    grades.append(score)

average = student_utils.get_average(grades)   # module name + dot
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)
status = get_status(average)                  # no module name needed

print("\n--- Your Report ---")
print("Generated on:", datetime.now().strftime("%B %d, %Y %I:%M %p"))
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest :", lowest)
print("Status :", status)
