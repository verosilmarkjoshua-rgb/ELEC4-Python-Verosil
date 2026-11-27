# Name: MARK JOSHUA VEROSIL
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 27, 2026

students = []         # LIST: keeps the names we display
names_seen = set()    # SET: lowercase names, used to catch duplicates


def add_student():
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    lower_name = name.lower()          # "Mark Joshua Verosil" and "mark joshua verosil" are the same
    if lower_name in names_seen:
        print("Duplicate! That student already exists.")
        return
    students.append(name.title())
    names_seen.add(lower_name)
    print("Added:", name.title())


def remove_student():
    name = input("Enter name to remove: ").strip().lower()
    if name not in names_seen:
        print("Student not found.")
        return
    for student in students:
        if student.lower() == name:
            students.remove(student)
            break
    names_seen.remove(name)
    print("Removed.")


def search_student():
    word = input("Search (partial name ok): ").strip().lower()
    matches = []
    for student in students:
        if word in student.lower():    # partial match - checks word is contained in student.lower()
            matches.append(student)
    if len(matches) == 0:
        print("No match found.")
    else:
        print("Found:")
        for student in matches:
            print("-", student)


def display_all():
    if len(students) == 0:
        print("No students yet.")
        return
    number = 1
    for student in sorted(students):   # alphabetical order
        print(str(number) + ".", student)
        number = number + 1
    print("Total:", len(students))


# ---------- Main program ----------

while True:
    print("\n=== Record Manager ===")
    print("1. Add  2. Remove  3. Search  4. Display all  5. Exit")
    menu_pick = input("Choose: ")

    if menu_pick == "1":
        add_student()
    elif menu_pick == "2":
        remove_student()
    elif menu_pick == "3":
        search_student()
    elif menu_pick == "4":
        display_all()
    elif menu_pick == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")


# Write your own 3-5 sentences here: list vs set, and where you used each.

# A list keeps items in order and can hold duplicates, while a set only keeps unique items and has no order.
# In my program, I used the list students to store the names because I need to display them and sort them alphabetically.
# I used the set names_seen to store the lowercase names because a set can quickly check if a name already exists.
# This helps me catch duplicates, like "Mark Joshua Verosil" and "mark joshua verosil", before adding a student to the list.
# When I remove a student, I remove the name from both the list and the set so they stay the same.
