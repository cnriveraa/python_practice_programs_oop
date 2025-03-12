# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function.

# initialize an empty list to store the numbers
numbers = []

# loop until invalid input is received
while True:
    try: 
        num = int(input("Enter a number: "))   # ask the user to input a number
        numbers.append(num)     # add the number to the list
        
# if input is not integer, print error message
# sort the numbers from lowest to highest
# display the numbers from lowest to highest