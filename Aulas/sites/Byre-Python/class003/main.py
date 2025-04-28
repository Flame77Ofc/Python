# while Statements
number = int(input("Enter a number: "))
if number >= 0:
    while number > 0:
        print(number)
        number = number - 1
else:
    while number < 0:
        print(number)
        number = number + 1