# Condicionais aninhadas
# São condições dentro de outras condições
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O primeiro número ({n1}) é maior que o segundo ({n2}) número")
elif n1 < n2:
    print(f"O primeiro número ({n1}) é menor que o segundo ({n2}) número")
else:
    print(f'Os dois números são iguais')



n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"A média é {media}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")