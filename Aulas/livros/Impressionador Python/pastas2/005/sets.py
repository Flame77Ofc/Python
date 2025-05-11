set1 = {'Laranja', 'Maçã', 'Abacaxi'}
set2 = {'Melancia', 'Laranja', 'Kiwi'}

sets = set1 | set2
set1 = set1.union(set2)
print(sets)
print(set1) 

set1.add('Pêra')
print(set1)

set1.discard('Pêra')
print(set1)