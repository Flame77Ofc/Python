# enumerate: Retorna o indíce (index) e o elemento
fruits = ["Apple", "Onion", "Banana", "Watermelon", "Orange", "Strawberry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


colors = ["Yellow", "Red", "Green", "Blue"]

for index, color in enumerate(colors):
    print(index, color)


# cars = ["Honda", "Lamborghini", "Ferrari", "Porsche", "Gol", "Brasília"]

# count = 0
# for car in cars:
#     print(car)
#     count += 1

# print(count)


cars = ["Honda", "Lamborghini", "Ferrari", "Porsche", "Gol", "Brasília"]

for index, car in enumerate(cars):
    print(car)

print(index+1)


animals = ["Panda", "Dog", "Cat", "Wolf", "Monkey", "Dolphin"]

for index, animal in enumerate(animals):
    print(index, animal)


characters = ["SpongeBob", "Luckey", "Patrick"]

index_character = []
for index, character in enumerate(characters):
    index_character.append([index, character])
    print(index, character)

print(index_character)  # [[0, 'SpongeBob'], [1, 'Luckey'], [2, 'Patrick']]


sellers = ["Marcos", "Julio", "João", "Felipe", "Maycon"]
prices = [50, 75, 125, 95, 345]

for index, seller in enumerate(sellers):
    print(prices[index], seller)


animals = ["Dog", "Cat", "Bird"]
prices = [5000, 2350, 1150]

for index, animal in enumerate(animals):
    print(prices[index], animal)


string = "Hello, World!"

# Way 1
index = 0
for letter in string:
    print(index, letter)
    index += 1

# Way 2
for index, letter in enumerate(string):
    print(index, letter)



# zip
usernames = ["angelical0123", "dudex888287", "manouwx92"]
passwords = ["GGBrawl123", "senha1234", "brasilsenha123"]

for username, password in zip(usernames, passwords):
    print(username, password)


characters = ["Pow", "Ben 10", "Colt", "Buzz Light Year", "Escanor"]
ages = [2, 10, 27, 35, 40]

for age, character in zip(ages, characters):
    print(age, character)


languages = ["Python", "JavaScript", "C++", "Java", "C", "C#", "COBOL", "Ruby"]
scores = [1000, 980, 995, 885, 980, 945, 650, 790]

for language, score in zip(languages, scores):
    print(f"{language:<12} {score}")


persons = ["Elon Musk", "Bill Gates", "Mark Zuckerberg", "Steve Jobs"]
ages = [54, 69, 41, 65]
fortunes = [445_000_000_000, 235_000_000_000, 127_000_000_000, 245_00_000_000]

for person, age, fortune in zip(persons, ages, fortunes):
    print(f"{person:<18} {age:<5} {fortune:<10}")
