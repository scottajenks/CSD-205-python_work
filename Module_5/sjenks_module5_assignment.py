# Scott Jenks - 8/27/2022 - Module 5 Assignment

# Calculate the cost of installing fiber optic cable

# importing decimal class
from decimal import *

print("Welcome to CSD 205 Fiber Optics! Thank you for choosing us for your fiber optic installation needs.")

# Ask for company name
company_name = input("\nWhat is the name of your company? ")

# ask for fiber optic length
len_fiber_optic = input("How many feet of fiber optics do you need? ")
# if input is not a number but a string, lets user know to input only a number
while not len_fiber_optic.isdigit():
    print("\nOnly enter a number.")
    len_fiber_optic = input("How many feet of fiber optics do you need? ")
else:
    len_fiber_optic = float(len_fiber_optic)

'''calculate the fiber optic lenth:
less than 100 feet = $0.87 per foot
more than 100 feet = $0.80 per foot
more than 250 feet = $0.70 per foot
more than 500 feet = $0.50 per foot'''

prices = [0.87, 0.80, 0.70, 0.50]

if len_fiber_optic < 100:
    total_price = len_fiber_optic * prices[0]
    print(
        f"\nThe price to install {len_fiber_optic:.0f} feet of fiber optics is ${prices[0]:.2f} per foot so the total price for {company_name.title().strip()}'s fiber optic installation is ${total_price:.2f}.")
elif len_fiber_optic < 250:
    total_price = len_fiber_optic * prices[1]
    print(
        f"\nThe price to install {len_fiber_optic:.0f} feet of fiber optics is ${prices[1]:.2f} per foot so the total price for {company_name.title().strip()}'s fiber optic installation is ${total_price:.2f}.")
elif len_fiber_optic < 500:
    total_price = len_fiber_optic * prices[2]
    print(
        f"\nThe price to install {len_fiber_optic:.0f} feet of fiber optics is ${prices[2]:.2f} per foot so the total price for {company_name.title().strip()}'s fiber optic installation is ${total_price:.2f}.")
else:
    total_price = len_fiber_optic * prices[3]
    print(
        f"\nThe price to install {len_fiber_optic:.0f} feet of fiber optics is ${prices[3]:.2f} per foot so the total price for {company_name.title().strip()}'s fiber optic installation is ${total_price:.2f}.")

# Exit program
input("\n\tPress ENTER to exit")

'''
References

https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string

https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python
'''
