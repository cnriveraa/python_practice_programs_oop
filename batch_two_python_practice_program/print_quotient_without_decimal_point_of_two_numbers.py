#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# print the quotient w/o decimal point
quotient = num1 // num2
print("The quotient is: ", quotient)