sexo = input("Qual o seu sexo? ").strip().upper()

while sexo not in ['M', 'F']:
    print("Sexo incorreto!")
    sexo = input("Qual o seu sexo? ").strip().upper()

if sexo == 'M':
    print("Você é do sexo Masculino")
else:
    print("Você é do sexo Feminino")