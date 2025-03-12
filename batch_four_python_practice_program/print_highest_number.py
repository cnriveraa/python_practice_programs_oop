# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number.

# initialize an empty list to store numbers
numbers = []

# ask user to input numbers
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)   # add numbers to the list
    except ValueError:
        print("Invalid input.")  # print error message if input is not integer
        break

# display the highest number
if num in numbers:    # check if the list is not empty
    print(f"The highest number is {max(numbers)}.")