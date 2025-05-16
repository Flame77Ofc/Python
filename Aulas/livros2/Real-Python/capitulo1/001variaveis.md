As variáveis são usadas para armazenar dados na memória de um computador na RAM (Random Access Memory)
Sintaxe Básica
A criação de uma variável em Python segue uma sintaxe simples:
nome_da_variavel = valor

Restrições para Nomes de Variáveis
1. Não devem começar com um número  
O nome de uma variável deve iniciar com uma letra (a-z, A-Z) ou um sublinhado (_). Começar com um número resulta em erro de sintaxe.
Exemplos errados:  
a. 2nome  
b. 35alunos  
c. 8gatos  
Exemplos corretos:  
a. gatos5  
b. animais45  
c. ma  
d. numero_2  

2. Não podem conter espaços nem caracteres especiais  
Hífens, pontos, ou outros caracteres especiais (como #, @, !) não são permitidos. O traço (_) é o único caractere especial permitido.
Exemplos incorretos:  
a. meu/nome  
b. casa-de-madeira  
c. usuarios#ativos  
Exemplos corretos:  
a. meu_nome  
b. usuarios_ativos  
c. casa_madeira  
d. valor_total  

3. São sensíveis a maiúsculas e minúsculas  
Python é case-sensitive, o que significa que letras maiúsculas e minúsculas são tratadas como diferentes. Por exemplo, Idade, idade e IDADE são consideradas variáveis distintas.

4. Não é permitido o uso de palavras reservadas 
Palavras reservadas do Python, como if, for, def, class, entre outras, não podem ser usadas como nomes de variáveis.
Aqui está uma tabela. Você não precisa decorar tudo, com tempo você aprende
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield


5. Não pode utilizar espaços
A comunidade python adotou uma forma de substituir os espaços pelo traço "_". O nome desse estilo é snake_case, onde as palavras que precisavam de espaços foram substituidas pelo traço.
Exemplo de snake_case:

nome_completo = "Maria Silva"  
total_de_alunos = 50


EXEMPLOS DE VARIÁVEIS






Múltiplas linhas e a docstring