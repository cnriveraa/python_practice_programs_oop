#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# loop the numbers from num1 + 1, not including num2
for i in range(num1 + 1, num2):
    print(i)