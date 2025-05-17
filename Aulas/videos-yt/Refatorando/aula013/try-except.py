try: # Executa normalmente se não houver nenhum erro
    numero = int(input('Digite um número '))
    
    print(numero)
except: # Executa se houver um erro
    print('Por favor, digite um número válido')
finally: # Sempre vai executar independente se houver ou não um erro
    print('Sempre executa')