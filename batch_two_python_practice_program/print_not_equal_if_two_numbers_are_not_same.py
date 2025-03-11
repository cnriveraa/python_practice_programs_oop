#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# check if the number are not equal
if num1 != num2:
    print("Not Equal")
else:
    print("Equal")