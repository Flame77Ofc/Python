# HAh
palavra = input('Digite a palavra: ').strip().lower() # A palavra da forca
for letra in palavra: # Para cada letra da palavra
    letra = palavra.split('_') # Então, separe cada palavra
ficticio = ['_' for repeticao in palavra] # Adiciona o caractere '_' para cada letra da palavra e armazena num list comprehensio


tentativas = 5
for d in range(tentativas):

    if '_' not in ficticio:
        print('Acabou! Você venceu! Parabéns!')
        break
    
    letra = input('Digite uma letra: ').strip()

    if len(letra) == 1:
        contador = 0
        for repeticao in palavra:
            if repeticao == letra:
                ficticio[contador] = letra
            contador += 1
        print(ficticio)
    
    else:
        print('Deve ser uma letra.')
    print(palavra)