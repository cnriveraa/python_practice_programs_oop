#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# loop from 1 to 100
for i in range (1, 101):
    if i % 10 != 0:        # check if number is not divisible by 10
        print(i)           # print the number if not ends with 0