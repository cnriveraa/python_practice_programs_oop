
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

# display all numbers, showing only the first entry of duplicates
print("Numbers (duplicates show only once):")

for num in numbers:
    if num not in seen:  # check if number has not seen before
        print(num)
        seen.add(num)   # add number to set of seen numbers