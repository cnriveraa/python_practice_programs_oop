#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# print the remainder when the first number is divided by the second number
remainder = num1 % num2
print("The remainder is: ", remainder)