# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# initialize an empty set to store the numbers
numbers = set()

# loop until invalid input is received
while True:
    try: 
        num = int(input("Enter a number: "))    # ask user to input a number

# check if the number is already in the set
# add unique number to the set
# if input is not integer, print error message
# exit loop if invalid input