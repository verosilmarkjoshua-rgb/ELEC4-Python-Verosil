# Full Name: Mark Joshua Verosil
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: November 26, 2026


# Name: MARK JOSHUA VEROSIL
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 24, 2026

grades = []   # GLOBAL variable: the list of grades


def enter_grades():
    global grades                     # so we can change the global list
    grades = []                       # start with an empty list
    count = int(input("How many grades will you enter? "))
    for i in range(count):
        grade = float(input("Enter grade " + str(i + 1) + " (0-100): "))
        while grade < 0 or grade > 100:
            print("Grade must be from 0 to 100.")
            grade = float(input("Enter grade " + str(i + 1) + " (0-100): "))
        grades.append(grade)
    print("Grades saved!")


def compute_average(grade_list):
    return sum(grade_list) / len(grade_list)


def get_status(average, passing=75):   # default argument: passing is 75
    if average >= passing:
        return "PASSED"
    else:
        return "FAILED"


def view_results():
    if len(grades) == 0:
        print("No grades yet. Choose option 1 first.")
        return
    average = compute_average(grades)  # LOCAL variable
    print("\n--- Results ---")
    print("Grades :", grades)
    print("Average:", round(average, 2))
    print("Highest:", max(grades))
    print("Lowest :", min(grades))
    print("Status :", get_status(average))


# ---------- Main program ----------

while True:
    print("\n=== Student Grade Calculator (MARK JOSHUA VEROSIL) ===")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")
    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        enter_grades()
    elif choice == "2":
        view_results()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")


# WRITE YOUR OWN 3-5 SENTENCES HERE (local vs global, using this program).

# A global variable is created outside of all functions, so every function in the program can use it.
# In my program, grades is a global variable because the menu options share the same list of grades.
# A local variable is created inside a function and only exists while that function is running.
# For example, average inside view_results() is local, so using it outside that function would cause an error.
# I used the global keyword in enter_grades() because I wanted to replace the global grades list instead of creating a new local one.
