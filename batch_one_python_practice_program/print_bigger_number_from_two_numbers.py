#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# print the bigger number
if num1 > num2:
    print("The bigger number is: ", num1)
else:
    print("The bigger number is: ", num2)