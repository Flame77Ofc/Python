def sayHello():
    print('Hello, World!')
sayHello()

def max_number(x, y):
    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is lower than {y}")
    elif x == y:
        print(f"{x} is equals to {y}")
max_number(89, 10298763)



def message():
    return('Hello!')
print(message())