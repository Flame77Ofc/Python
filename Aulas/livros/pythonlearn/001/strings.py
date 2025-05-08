fruit = 'banana'
letter = fruit[1]
print(letter)

length = len(fruit)
print(length)

for char in fruit:
    print(char, end=' ')


phrase = 'I love learning Python!'
slicing = phrase[5:12]
slicing = phrase[:9]
slicing = phrase[16:]

'love' in phrase
'learn' in phrase
'JavaScript' not in phrase

word = 'Hello, World!'
dir(word)

word.upper()
word.lower()
word.capitalize()
word.title()

indexText = word.index('e') # Retorna em qual índice a letra está

stripText = '  My text '
stripText.strip() # Remove os espaços

text = 'I like cats'
text.startswith('I')
text.endswith('cats')