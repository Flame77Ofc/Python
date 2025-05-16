# Condicionais: Permite que o programa tome decisões através de condições verdadeiras
# Dependendo da condição, o programa executará um bloco de código diferente. 
# sintaxe
# if condição:
    # <bloco de codigo>

# Vamos ver na prática
lampada = True # Declarando uma variável, que significa que a luz está acessa
if lampada == True: # O programa verifica se essa condição é verdadeira e executa esse bloco de código:
    print('A lampada está acessa') # Então se a lampada estiver acessa o programa executará este bloco de código.
else: # Mas se a condição for falsa, então o programa executará este bloco de código:
    print('A lampada está apagada') # Imprimirá 'A lampada está apagada'

# Não há limite de condições para verificar, podem ser quantas você quiser.
# Vejamos mais alguns exemplos:
# O programa verifica em que hora do dia estamos.
hora = 7
if hora < 12: # Se hora for menor que 12, ou seja, se for antes do meio dia, então será Manhã
    print('Manhã')
elif hora < 18: # Mas se a hora for menor que 18, ou seja, se for antes odo meio dia, então será Tarde
    print('Tarde')
elif hora >= 24: # Tratamento de Erros
    print('Não existe mais de 24 horas num dia!')
else: # A última opção é Noite, ou seja, se não for nenhuma das opções acima, exceutará este bloco de código.
    print('Noite')