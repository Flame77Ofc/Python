# for loop → você geralmente sabe quantas iterações vai ter. # for → geralmente número fixo ou previsível de vezes
for i in range(5):
    print(i) 
# Você sabe que ele vai rodar 5 vezes: i = 0, 1, 2, 3, 4.

for letra in "abc":
    print(letra) 
# Você sabe que vai rodar 3 vezes, porque "abc" tem 3 letras.
  

for i in range(3):
  print(i) # resultado = 0, 1, 2
# a instrução range (N) gera uma lista com N números, onde o primeiro número é 0 e o último é N - 1.


# # while → depende de uma condição, pode ser imprevisível. while loop → você geralmente NÃO sabe quantas iterações vai ter. Porque ele depende de uma condição que pode mudar dinamicamente:
while x < 10:
    x += 1 # Aqui, quantas vezes vai rodar depende de quanto vale x no início. Pode ser 10 vezes, 5 vezes ou nenhuma.

while True:
    comando = input("Digite 'sair' para parar: ")
    if comando == 'sair':
        break
# Você não tem ideia de quantas vezes a pessoa vai digitar algo antes de escrever 'sair' 