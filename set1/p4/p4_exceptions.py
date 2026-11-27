# Name: MARK JOSHUA VEROSIL
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 27
# , 2026


def divide_numbers():
    try:
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))
        answer = first_number / second_number
    except ValueError:
        print("Error: please type numbers only.")
    except ZeroDivisionError:
        print("Error: you cannot divide by zero.")
    else:
        print("Result:", answer)                  # runs only if no error happened
    finally:
        print("(Division attempt finished)")      # always runs


def open_file():
    file_name = input("File name: ")
    try:
        my_file = open(file_name, "r")
        print(my_file.read())
        my_file.close()
    except FileNotFoundError:
        print("Error: that file does not exist.")
    finally:
        print("(File attempt finished)")          # always runs


# ---------- Main program ----------

while True:
    print("\n=== Safe Menu ===")
    print("1. Divide  2. Open file  3. Exit")
    menu_pick = input("Choose: ")

    if menu_pick == "1":
        divide_numbers()
    elif menu_pick == "2":
        open_file()
    elif menu_pick == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
