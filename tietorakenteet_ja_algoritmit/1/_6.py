"""
12
6
11
0
The total is now 12.0
The total is now 18.0
The total is now 29.0
The grand total is 29.0

"""


total = 0

input_number = ""
while input_number != 0:
    try:
        input_number = float(input())
        if input_number != 0:
            total += input_number
            print(f'The total is now {total:.1f}')

    except ValueError:
        print("That wasn’t a number.")

print(f'The grand total is {total:.1f}')