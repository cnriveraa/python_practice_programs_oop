#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# initialize a variable 'odd' to count the number of odd numbers entered
odd = 0

# start a loop that will iterate 10 times (from 0 to 9)
for i in range(10):
    num = int(input("Enter a number: "))   # ask user to input a number

# check if the number is odd
    if num % 2 != 0:
        odd += 1    # increment the 'odd' by 1