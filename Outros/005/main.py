# Lambda Functions
Minhalambda = lambda num : num * 2
sum = lambda x,y: x + y
print(sum(5, 3))


# Map
numbers = [1,2,3]
def duplo(a):
    return a * 10
result = map(duplo, numbers)
print(list(result))