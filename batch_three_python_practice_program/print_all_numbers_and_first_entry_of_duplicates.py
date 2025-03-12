
# initialize an empty list to store numbers
numbers = []

# ask user to input 10 numbers
for i in range(10):
    while True:  # loop until valid input is received
        try: 
            num = int(input(f"Enter number {i + 1}: "))