# Exceções e Tratamento de Erros
# Num programa, pode ter, em algum momento erros. Erros de qualquer tipo, seja de indentacao, entrada de usuário, uma operação que retornou um resultado inesperado, uma saída inesperada, etc. A boa notícia é que você você tratar esses erros. Quando acontece algum erro, o interpretador diz um texto gigante todo em vermelho e em inglês, que se o usuário lesse, não entenderia nada. É justamente pra isso que serve a exceção e tratamento de erros: mostrar ao usuário uma mensagem mais amigável e significativa. Vamos ver como podemos tratar erros:
# sintaxe básica:
# try:
#     <bloco de código>
# except:
#     <mensagem de erro>

# primeiro de tudo utilizamos a palavra-chave try com os dois pontos e logo em seguida o bloco de comandos que você acha que dará algum erro indentado, indicando que faz parte da estrutura do try. após o bloco de código, é utilizado a palavra-chave exception fora da indentacao do try. O except será executado apenas se o bloco de código do try resultar em algum erro.

# exemplo:
try:
    divisao = 3 / "string"
    print(divisao) # Isso sempre dará um erro porque não é possível dividir um inteiro por uma string.
except:
    print("Ocorreu um erro!")

# saída: Ocorreu um erro!
# Exceções são essenciais num programa para mostrar uma mensagem menos assustadora. Além desse tipo geral, existe também exceções específicas que você pode tratar. No exemplo acima, apenas tratamos os erros gerais, ou seja, se fosse um erro de sintaxe, indentacao ou qualquer outra coisa, sempre mostraria a mesma mensagem sempre. Vamos conhecer as exceções específicas: