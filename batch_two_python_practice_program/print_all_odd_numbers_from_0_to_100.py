#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# loop the numbers from 0 to 100 with a step of 1
for i in range(0, 101, 1):

    # check if the number is odd
    if i % 2 != 0:
        print(i)

# Note: 'I' should be 'i' to reference the variable correctly