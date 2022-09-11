# Scott Jenks - 9/11/2022 - Module 8 Assignment

# Program using function to convert miles to kilometers


def mileage_conversion():
    '''Get mileage driven and convert to kilometers'''

# Ask user for miles driven
    miles = input("\nHow many miles did you drive? ")
    try:
        miles = float(miles)
    except ValueError:
        print("\tPlease only enter a numerical value.\n")
        miles = input("How many miles did you drive today? ")
        miles = float(miles)

# Convert miles driven into kilometers and print
    kilometers_driven = miles * float(1.609344)

    if kilometers_driven < 1:
        print(
            f"\nYou drove {miles:.2f} mile which is equivelant to {kilometers_driven:.2f} kilometer.")
    elif miles <= 1:
        print(
            f"\nYou drove {miles:.2f} mile which is equivelant to {kilometers_driven:.2f} kilometers.")
    else:
        print(
            f"\nYou drove {miles:.2f} miles which is equivelant to {kilometers_driven:.2f} kilometers.")


print("Lets convert your milage to see how many kilometers you drove today!")

# Use mileage_conversion funtion
mileage_conversion()

#Repeat or quit
print("\nDid you take another road trip?")
while True:
    answer = input("\tType 'Y' to report or 'N' to quit. ")
    answer = answer.title()
    if answer == 'N':
        break
    else:
        mileage_conversion()
