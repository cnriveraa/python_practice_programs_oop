#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# ask user to input 10 numbers using list comprehension
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# store the first number from the list for later use
first_number = numbers[0]

# loop the remaining numbers from the list (from 2nd to last)
for num in numbers[1:]:
    print(f"{first_number} - {num} = {first_number - num}")