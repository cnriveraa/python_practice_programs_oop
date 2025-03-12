# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize an empty set to store numbers
numbers = []

# ask user to input 10 numbers
for i in range(10):
    while True:  # loop until valid is received
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)  # add number to the list
            break                # exit the loop if invalid input
        except ValueError:
            print("Invalid input.")  # print error message

# initialize a set to track duplicates
duplicates = set()

# find duplicates
for num in numbers:
    if numbers.count(num) > 1:   # check if the number has duplicates
        duplicates.add(num)      # add duplicates to the set
        
# display duplicates