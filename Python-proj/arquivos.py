# Arquivos: O Python permite que você leia e modifique o conteúdo de arquivos! Lembrando que nesse curso, vamos focar nos arquivos de texto, aqueles com a extensão '.txt'. Vamos lá. Imagine que você precise ler o conteúdo de um arquivo ou até alterar ele.
# Que tal fazer isso com Python? É simples e poderoso!

# Primeira coisa: pra mexer em um arquivo, a gente precisa abrir ele, certo? Então vamos aprender a abrir arquivos com Python.

# A sintaxe básica pra isso é:
# open(nome_do_arquivo, modo, encoding)

# Agora vamos entender o que cada parte dessa função faz:
# - nome_do_arquivo: o nome do arquivo que você quer acessar. Simples assim.
# - modo: o que você vai fazer com o arquivo? Ler? Escrever? Adicionar mais conteúdo?
# - encoding: define como o texto será codificado. Usamos 'utf-8' pra aceitar acentos, emojis e caracteres especiais.

# Vamos ver os modos mais comuns:
"""
w  - write: escreve no arquivo, apagando tudo o que tinha antes (cuidado!)
r  - read: só lê o conteúdo do arquivo
a  - append: adiciona conteúdo no final, sem apagar o que já tinha
a+ - append and read: adiciona conteúdo e também permite leitura
"""

# Vamos ver isso funcionando na prática!

# Primeiro, criamos uma variável chamada 'arquivo', e abrimos um arquivo pra escrita ('w'):
arquivo = open('arquivo.txt', 'w', encoding='utf-8')

# Aqui a gente criou (ou sobrescreveu) um arquivo chamado 'arquivo.txt'.
# Estamos usando o modo 'w', que vai apagar qualquer conteúdo antigo e escrever do zero.
# Também usamos encoding='utf-8' pra garantir que acentuação e caracteres especiais funcionem.

# Agora vamos escrever alguma coisa nesse arquivo:
arquivo.write('Escrevendo coisas aqui')

# Pronto! Quando esse código é executado, ele cria o arquivo (se não existir) e escreve exatamente o que colocamos no .write(). Fácil, né?

# Agora vamos ver como a gente lê o conteúdo de um arquivo.
# Pra isso, usamos o modo 'r':
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())  # saída esperada: Escrevendo coisas aqui

# Legal! Agora vamos conhecer o modo 'a', que é usado pra adicionar conteúdo sem apagar o que já tinha:
arquivo = open('arquivo.txt', 'a', encoding='utf-8')
arquivo.write('Escrevendo coisas aqui novamente!')

# Vamos ler o conteúdo de novo e ver como ficou:
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())

# saída:
"""
Escrevendo coisas aqui
Escrevendo coisas aquiEscrevendo coisas aqui novamente!
"""

# Repara que o texto ficou tudo grudado. Isso acontece porque o write() escreve exatamente como a gente manda, e não coloca uma quebra de linha automática. Porém a solução é simples: apenas usar '\n' pra pular pra próxima linha.

# Vamos corrigir isso:
arquivo = open('arquivo.txt', 'a', encoding='utf-8')
arquivo.write('\nEscrevendo coisas aqui novamente!')

# Agora sim, tudo organizadinho!
arquivo = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo.read())

# saída:
"""
Escrevendo coisas aqui
Escrevendo coisas aqui novamente!
"""

# Legal demais, né? Agora deixa eu te mostrar um truque profissional: Ao invés de abrir e fechar arquivos manualmente, dá pra usar o 'with'. É um método mais seguro para abrir arquivos e modificá-los. Vamos ver:

# Veja só como usar:
with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nMais uma linha adicionada com segurança!')

# Aqui usamos o 'with open(...) as arquivo', o que significa que ele automaticamente fecha o arquivo, evitando desastres posteriores.