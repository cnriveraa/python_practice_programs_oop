#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# loop numbers from 0 to 100 with step of 1
for i in range(0, 101, 1):
    if i % 10 != 0 and i % 10 != 5:      # check if number does not end with 0 or 5
        print(i)