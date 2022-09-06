# Scott Jenks - 8/15/2022 - Module 3 Assignment

# Calculate the cost of installing fiber optic cable

print("Welcome to CSD 205 Fiber Optics! Thank you for choosing us for your fiber optic installation needs.")

# Ask for company name
company_name = input("\nWhat is the name of your company? ")

# ask for fiber optic length
len_fiber_optic = (input("How many feet of fiber optics do you need? "))
# if input is not a number but a string, lets user know to input only a number
while not len_fiber_optic.isdigit():
    print("\nOnly enter a number.")
    len_fiber_optic = input("How many feet of fiber optics do you need? ")
# changes integer to float
else:
    len_fiber_optic = float(len_fiber_optic)

# calculate the fiber optic lenth by 0.87 per foot
price = float(0.87)
total_price = len_fiber_optic * price

# format total_price to two decimal places
#format_total_price = "{:.2f}".format(total_price)

print(
    f"\nThe price to install fiber optics is $0.87 per foot so the total price for {company_name.title().strip()}'s fiber optic installation is ${total_price:.2f}.")

# Exit program
input("\n\tPress ENTER to exit")

'''
References
Kevin, N. A. (2018, November 6). Input in python to be only in String. Stack Overflow. Retrieved August 15, 2022, from https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string 

Kumar, B. (2020, December 11). Python print 2 decimal places. Python Guides. Retrieved August 15, 2022, from https://pythonguides.com/python-print-2-decimal-places/ 
'''
