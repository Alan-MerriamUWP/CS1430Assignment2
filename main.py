"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (SEMESTERS_PER_YEAR * credits)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return annual_cost / SEMESTERS_PER_YEAR / credits * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


def cost_per_minute(annual_cost, credits):
    """Give back what one minute of a 50-minute CS 1430 class meeting costs."""
    return cost_per_class(annual_cost, credits) / 50


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = float(input("Enter the number of credits taken this semester: "))
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.

    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost per minute")
        print("Q. Quit")
        choice = input("Choose an option: ")
        if choice == "Q":
            break
        elif choice == "1":
            print("Cost per semester: ${:.2f}".format(cost_per_semester(annual_cost)))
        elif choice == "2":
            print("Cost per month: ${:.2f}".format(cost_per_month(annual_cost)))
        elif choice == "3":
            print("Cost per day: ${:.2f}".format(cost_per_day(annual_cost)))
        elif choice == "4":
            print("Cost per credit: ${:.2f}".format(cost_per_credit(annual_cost, credits)))
        elif choice == "5":
            print("Cost per class: ${:.2f}".format(cost_per_class(annual_cost, credits)))
        elif choice == "6":
            print("Cost per minute: ${:.2f}".format(cost_per_minute(annual_cost, credits)))
        else:
            print("Invalid choice. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
