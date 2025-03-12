
# initialize an empty list to store numbers
numbers = []

# ask user to input 10 numbers
for i in range(10):
    while True:  # loop until valid input is received
        try: 
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)  # add number to the list
            break
        except ValueError:
            print("Invalid input.")  # handle invalid input

# initialize an empty set to track seen numbers
seen = set()