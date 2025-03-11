# For loop
"""
for variable in sequence:
    statement(s)
"""
# # For loop in lists
pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(pet)

# For loop in strings
txt = 'Hello, Wolrd!'
for words in txt:
    print(words)

# For loop in range
for i in range(1,11):
    print('Hello, World!')

# For loop in nested lists
animal = ['tiger', 'cat', 'horse']
sound = ['roars', 'meows', 'nhaaww']
for x in animal:
    for y in sound:
        print('the ' + x + ' ' + y)
        
# For loop in else
for a in range(1, 4):
    print('Hello, World!', a)
else:
    print('Loop ends!')