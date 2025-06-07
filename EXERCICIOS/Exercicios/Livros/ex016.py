# Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso custa US$15. Escreva um loop que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
preco = 0
pessoas = int(input('São quantas pessoas? '))
for i in range(pessoas):
  idade = int(input(f'Digite a idade da pessoa {i+1}: '))

  if idade < 3: # Se idade for menor que 3, ingresso gratuito
    ingresso = 0
  elif idade >= 3 and idade <= 12: # Se idade estiver entre 3 e 12, ingresso custa 10 reais.
    ingresso = 10
  elif idade > 12: # Se idade for maior que 12, ingresso custa 15 reais
    ingresso = 15
  
  preco += ingresso

print(f"O preço total dos ingressos é de R${preco} reais.")
