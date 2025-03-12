# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize an empty set to store numbers
numbers = []

# ask user to input 10 numbers
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input.")

# initialize a set to track duplicates
# find duplicates
# display duplicates