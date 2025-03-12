# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

# initialize an empty list to store the number
numbers = []

# loop until invalid input is received
while True:
    try:
        num = int(input("Enter a number: "))    # ask user to input a number
        numbers.append(num)    # add the number to the list
    
    except ValueError:
        print("Invalid input.")     # error message if non-integer input

        if len(numbers):
            print(f"The lowest number is: {min(numbers)}")  # display lowest number
            break