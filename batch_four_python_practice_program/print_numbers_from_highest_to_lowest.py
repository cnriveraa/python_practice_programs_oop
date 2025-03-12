# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function.

# initialize an empty list to store numbers
numbers = []

# ask user to input numbers
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)  # add numbers to the list
    except ValueError:
        print("Invalid input.")   # error message for non-integers input
        break

# sort the numbers from highest to lowest
numbers.sort(reverse=True)    # reverse sort function

# display the number from highest to lowest
if num in numbers:
    print("Numbers from highest to lowest: ", numbers)