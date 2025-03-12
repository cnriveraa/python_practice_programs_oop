# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# initialize an empty list to store numbers
numbers = []

# start loop to iterate numbers
while True: 
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input.")
        break

# find the average