# Prog02: Create a program that asks the user to input numbers and displays the number with the most duplicates. The program continues asking for input until the user enters an invalid input.

# initialize a list to store numbers
numbers = []

# ask the user to input numbers
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)   # add numbers to the list 
    except ValueError:
        print("Invalid input.")  # error message if non-integer input
        break

# check if any numbers were entered
if numbers:
    count_dict = {}    # initialize a dictionary to count occurrences of each number

    # count entries of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # find the number with the most duplicates
    most_duplicates_num = None
    max_count = 0

    for num, count in count_dict.items():
        if num > max_count:
            max_count = count
            most_duplicates_num = num

# display the result