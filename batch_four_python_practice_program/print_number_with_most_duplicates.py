# Prog02: Create a program that asks the user to input numbers and displays the number with the most duplicates. The program continues asking for input until the user enters an invalid input.

# initialize a list to store numbers
numbers = []

# ask the user to input numbers
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input.")
        break

# check if any numbers were entered
# find the number with the most duplicates
# display the result