6.7 Pessoas: comece com o programa escrito para Exercício 6.1 (página 138). Crie dois dicionários novos representando pessoas diferentes e armazene todos os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um loop. À medida que percorre a lista,
exiba tudo o que sabe sobre cada pessoa.
6.8 Animais de estimação: Crie vários dicionários, em que cada dicionário representa um animal de estimação diferente. Em cada dicionário inclua o tipo de animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets. Depois, percorra sua lista com um loop e, enquanto faz isso, exiba tudo o que sabe sobre cada animal de estimação. 
6.9 Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chave no dicionário e armazene de um a três lugares favoritos para cada pessoa.
Agora, para que este exercício fique ainda mais interessante, peça a alguns amigos que lhe
digam alguns de seus lugares favoritos. Percorra o dicionário com um loop e exiba o nome de
cada pessoa e seus lugares favoritos.
6.10 Números favoritos: Modifique seu programa do Exercício 6.2 (página 138) para que cada
pessoa possa ter mais de um número favorito. Depois, exiba o nome de cada pessoa com seus
números favoritos.
6.11 Cidades: Crie um dicionário chamado cities. Utilize o nome de três cidades como chaves de
seu dicionário. Crie um dicionário de informações sobre cada cidade e inclua o país em que a
cidade está, sua população aproximada e um fato sobre essa cidade. O nome das chaves para o
dicionário de cada cidade devem ser alguma coisa como country, population e fact. Exiba o
nome de cada cidade e todas as informações que você armazenou a respeito.
6.12 Extensões: Agora que já estamos trabalhando com exemplos complexos o suficiente para
que sejam mais desenvolvidos de diferentes maneira, use um dos programas de exemplo deste
capítulo e o amplie, adicionando chaves e valores novos, alterando o contexto do programa ou
melhorando a formatação da saída.


7.4 Ingredientes de pizza: Escreva um loop que solicite ao usuário uma série de ingredientes de
pizza até que ele forneça o valor 'quit'. À medida que cada ingrediente é fornecido, exiba uma
mensagem informando que esses ingredientes estão sendo adicionados à pizza.
7.5 Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade
da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o
ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso custa US$15. Escreva um loop
que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
7.6 Três saídas: Crie diferentes versões do Exercício 7.4 ou 7.5 que executem cada uma das
seguintes tarefas, pelo menos uma vez:
• Use um teste condicional na instrução while para interromper o loop.
• Use uma variável active para controlar o tempo que o loop é executado.
• Use uma instrução break para sair do loop quando o usuário inserir o valor 'quit'.
7.7 Infinito: Escreva e execute um loop infinito. (Para encerrar o loop, pressione CTRL+C ou
feche a janela que exibe a saída.)


7.8 Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com o nome de diversos
sanduíches. Depois, crie uma lista vazia chamada finished_sandwiches. Percorra a lista de
pedidos de sanduíches com um loop e exiba uma mensagem para cada pedido, como: Seu lanche
de atum está pronto. Conforme cada sanduíche é preparado, passe-os para a lista de sanduíches
prontos. Após todos os sanduíches terem sido preparados, exiba uma mensagem enumerando
cada um deles.
7.9 Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, assegure-se de que o
sanduíche 'pastrami' apareça na lista pelo menos três vezes. Faça mais um código perto do início
de seu programa, exibindo uma mensagem que informe que a lanchonete está sem pastrami e,
em seguida, use um loop while para remover todas as ocorrências de 'pastrami' em
sandwich_orders. Faça questão de que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
7.10 Férias tão sonhadas: Crie uma pesquisa que pergunte aos usuários sobre as férias de seus sonhos. Crie um prompt mais ou menos assim: Se pudesse visitar qualquer lugar do mundo, para onde iria? Inclua um bloco de código que exiba os resultados dessa pesquisa.


8.3 Camiseta: Crie uma função chamada make_shirt() que aceita um tamanho e o texto que deve ser estampado na camiseta. A função deve exibir uma frase resumindo o tamanho da camiseta e a mensagem estampada nela. Chame a função uma vez usando argumentos posicionais para criar uma camiseta. Chame a função uma segunda vez usando argumentos nomeados.
8.4 Camisetas grandes: Modifique a função make_shirt() para que as camisetas sejam grandes por padrão com a seguinte frase estampada: Eu amo Python. Escreva uma camiseta grande e uma média com a mensagem padrão e uma camiseta de qualquer tamanho com uma frase diferente.
8.5 Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma cidade e de seu país. A função deve exibir uma simples frase, como Reykjavik fica na Islândia. Forneça ao parâmetro do país um valor default. Chame sua função para três cidades diferentes e, pelo menos, para uma que não esteja no país default.

8.6 Nome de cidades: Escreva uma função chamada city_country() que recebe o nome de uma cidade e seu país. A função deve retornar uma string formatada como esta: "Santiago, Chile" Chame sua função com pelo menos três pares cidade-país e exiba os valores retornados.
8.7 Álbum: Escreva uma função chamada make_album() que crie um dicionário representando um álbum de música. A função deve ter o nome de um artista e o título de álbum, e deve retornar um dicionário com essas duas informações. Utilize a função para criar três dicionários representando álbuns distintos. Exiba cada valor de retorno para mostrar que os dicionários estão armazenando adequadamente as informações do álbum. Use None para adicionar um parâmetro opcional ao make_album() que possibilite armazenar o
número de músicas em um álbum. Se a linha chamadora incluir um valor para o número de
músicas, adicione esse valor ao dicionário do álbum. Crie, pelo menos, uma nova chamada de
função que inclua o número de músicas em um álbum.
8.8 Álbuns de usuários: Comece com seu programa do Exercício 8.7. Escreva um loop while que
possibilite aos usuários inserir o artista e o título de um álbum. Após receber essas informações,
chame make_album() com a entrada do usuário e exiba o dicionário criado. Não se esqueça de
incluir um valor de saída no loop while.

8.9 Mensagens: Crie uma lista com uma série de mensagens curtas de texto. Passe a lista para uma função chamada show_messages(), que exiba cada mensagem de texto.
8.10 Enviando mensagens: Comece com uma cópia do seu programa do Exercício 8.9. Escreva uma função chamada send_messages() para exibir cada mensagem de texto e passe cada mensagem para uma nova lista chamada sent_messages à medida que é exibida. Após chamar a função, exiba ambas as listas para ter certeza de que as mensagens foram corretamente transferidas.
8.11 Mensagens arquivadas: Comece sua tarefa a partir do Exercício 8.10. Chame a função send_messages() com uma cópia da lista de mensagens. Após chamar a função, exiba ambas as listas para mostrar que a lista original reteve suas mensagens.


9.1 Restaurante: Crie uma classe chamada Restaurant. O método __init__() para Restaurant deve
armazenar dois atributos: restaurant_name e cuisine_type. Crie um método chamado
describe_restaurant() que exiba essas duas informações e um método chamado open_restaurant()
que exiba uma mensagem sinalizando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois atributos
individualmente e, em seguida, chame ambos os métodos.
9.2 Três restaurantes: Comece com sua classe do Exercício 9.1. Crie três instâncias diferentes da
classe e chame describe_restaurant() para cada instância.
9.3 Usuários: Crie uma classe chamada User. Crie dois atributos chamados first_name e
last_name e diversos outros atributos que normalmente são armazenados em um perfil de
usuário. Crie um método chamado describe_user() que exiba um resumo das informações do
usuário. Crie outro método chamado greet_user() que exiba um cumprimento personalizado ao usuário.
9.4 Pessoas atendidas: Comece com o seu programa do Exercício 9.1 (página 208). Adicione um
atributo chamado number_served com um valor default de 0. Crie uma instância chamada
restaurant a partir dessa classe. Exiba o número de clientes que o restaurante atendeu e, em
seguida, altere este valor e o exiba novamente.
Adicione um método chamado set_number_served() que possibilita definir o número de clientes
atendidos. Chame esse método com um novo número e exiba mais uma vez o valor.
Adicione um método chamado increment_number_served(), o qual possibilita aumentar o
número de clientes atendidos. Chame esse método com qualquer número que quiser e que possa
representar quantos clientes foram atendidos em, digamos, um dia de atividade comercial.
9.5 Tentativas de login: Adicione um atributo chamado login_attempts à sua classe User do
Exercício 9.3 (página 209). Crie um método chamado increment_login_attempts() que
incrementa o valor de login_attempts em 1. Crie outro método chamado reset_login_attempts()
que redefine o valor de login_attempts para 0.
Crie uma instância da classe User e chame increment_login_attempts() diversas vezes. Exiba o
valor de login_attempts para verificar que foi incrementado corretamente e, em seguida, chame
reset_login_attempts(). Exiba login_attempts novamente a fim de ter certeza de que foi
redefinido para 0.