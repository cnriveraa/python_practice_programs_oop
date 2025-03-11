#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# initialize a variable 'even' to count the number of even numbers entered by the user
even = 0

# start a loop that will iterate 10 times
for i in range(10):
    num = int(input("Enter a number: ")) n     # ask user to input a number

    # check if the number is even
    if num % 2 == 0:
        even += 1         # if even, increment by 1
        print("The total of even numbers is: ", even)

# Note: The print statement inside the loop will display the count after each input.
# If you want to display the total count only once after all inputs, move the print statement outside the loop.