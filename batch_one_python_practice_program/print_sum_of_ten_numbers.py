#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# initialize a variable 'sum' to store the total sum of the numbers
sum = 0

# start a loop that will iterate 10 times (from 0 to 9)
for i in range(10): 
    num = int(input("Enter a number: "))    # ask user to input a number
    sum += num                              # add the number to the 'sum' variable

# print the current total sum of all the numbers entered so far
print("The sum of all the numbers is:", sum)