# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

# initialize an empty list to store the number
numbers = []

# loop until invalid input is received
while True:
    try:
        num = int(input("Enter a number: "))    # ask user to input a number
        
# error message if non-integer input
# display lowest number