# Scott Jenks - 9/19/2022 - Module 10 Assignment

# Program using json to ask user for information and save it to file of their choosing.

# import the  OS library
import os
# import json library
import json

# Ask user which directory they would like to save the file too
directory_name = input("Which directory would you like to save the file too? ")

# See if directory exists
if os.path.isdir(directory_name):
    print("That directory exists.")

# Ask user which file they would like to save too
filename = input(
    "\nWhat would you like to name the file to save your information to be called? ")
filename = f'{filename}.txt'

# See if file exists
if os.path.isfile(filename) == True:
    overwrite_doc = input(
        "\nThe file already exists. Would you like to overwrite it? 'Y' - 'N': ")
    overwrite_doc = overwrite_doc.title()

# If user would like to override file continue
    if overwrite_doc == "Y":
        pass
    else:
        # Ask user which file they would like to save too
        filename = input(
            "\nWhat would you like to name the file to save your information to be called? ")
        filename = f'{filename}.txt'

# Combine directory and filename
complete_path = directory_name + filename

# Ask user for their information
fname = input("\nWhat is your first name? ")
lname = input("What is your last name? ")
address1 = input("What is your house address? ")
city = input("What city do you live in? ")
state = input("What state do you live in? ")
zipcode = input("What is your zipcode? ")
area_code = input("What is the area code for your phone number? ")
phone_number = input("What is your phone number? ")

# Combine information
full_name = f"{fname} {lname}"
full_address = f"{address1}, {city}, {state} {zipcode}"
full_phone_number = f"({area_code}) {phone_number}"


# Open the file in the directory and write the user information
with open(complete_path, 'w') as f:
    f.write(f"{full_name}\n")
    f.write(f"{full_address}\n")
    f.write(f"{full_phone_number}\n")
    print(
        f"\nThank you {full_name.title()}. We have saved your address and phone number to {complete_path}.")

# Ask user if they would like to verify their information
answer = input(
    "\n\tWould you like to verify your information is correct? 'Y' - 'N': ")
answer = answer.title()

if answer == 'Y':
    with open(complete_path) as file:
        for line in file:
            print(line.rstrip())
        input("\n\t\tPress Enter to quit.")
else:
    input("\n\t\tPress Enter to quit.")
