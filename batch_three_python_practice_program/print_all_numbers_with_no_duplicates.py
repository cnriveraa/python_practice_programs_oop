# Prog01: Create a program that asks the user to input 10 numbers and displays all numbers that don't have duplicates.

# initialize an empty list to store the numbers
numbers = []

# ask the user to input 10 numbers
for i in range(10):
    while True:  # Loop until valid input is received
        try:
            num = int(input("Enter a number: "))