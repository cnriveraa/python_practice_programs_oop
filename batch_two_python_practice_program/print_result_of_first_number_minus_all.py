#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# ask user to input 10 numbers using list comprehension
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# store the first number from the list for later use
first_number = numbers[0]