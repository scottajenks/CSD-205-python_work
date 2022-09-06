# Scott Jenks - 9/6/2022 - Module 7 Assignment

# Program determining how long it will take to an investment to double at a given interest rate.

starting_investment = input(
    "Please give me a number of how much do you have to invest? ")
starting_investment = float(starting_investment)

rate = input("What is your interest rate? ")
rate = float(rate)
interest_rate = rate / 100

# Simple Interest
print("\nPlease see below for simple interest:")
year_total = (starting_investment * interest_rate) + starting_investment
total_years = 1
print(
    f"\tAfter {total_years} year your investment amount is ${year_total:.2f}.")

while year_total < starting_investment * 2:
    year_total = (starting_investment * interest_rate) + year_total
    total_years = total_years + 1
    print(
        f"\tAfter {total_years} years your investment amount is ${year_total:.2f}.")
else:
    print(f"After {total_years} years your investment has doubled!")

# Compounded Interest
print("\nPlease see below for compounded interest:")
year_total = (starting_investment * interest_rate) + starting_investment
total_years = 1
print(
    f"\tAfter {total_years} year your investment amount is ${year_total:.2f}.")

while year_total < starting_investment * 2:
    year_total = (year_total * interest_rate) + year_total
    total_years = total_years + 1
    print(
        f"\tAfter {total_years} years your investment amount is ${year_total:.2f}.")
else:
    print(f"After {total_years} years your investment has doubled!")

input("\n\t\tPress Enter to exit.")
