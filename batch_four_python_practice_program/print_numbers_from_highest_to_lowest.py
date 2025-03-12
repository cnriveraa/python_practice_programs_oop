# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function.

# initialize an empty list to store numbers
numbers = []

# ask user to input numbers
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input.")
        break

# sort the numbers from highest to lowest
numbers.sort(reverse=True)

# display the number from highest to lowest