#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# check if the numbers are equal
if num1 == num2:
    print("Equal")
else:
    print("Not Equal")