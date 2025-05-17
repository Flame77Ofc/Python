# pede ao usuário adicionar um todo
def archive():
    global arquivo
    with open('proj/tarefas.txt', 'a+', encoding='utf-8') as arquivo:
        for i in lista_todo:
            arquivo.write(f'- {i}\n')

def ler():
    global arquivo
    with open('proj/tarefas.txt', 'a+', encoding='utf-8') as arquivo:
        arquivo.seek(0)
        print(arquivo.read())

def view(mensagem):
    print(mensagem.center(50, '-'))
    for i in lista_todo:
        print(f'- {i}')


def remover():
    with open('proj/tarefas.txt', 'a+', encoding='utf-8') as arquivo:
        arquivo.seek(0)
        leitura = arquivo.read()
        remove = input("Qual Tarefa deseja remover ou já concluiu? ")
        for i in range(1, 100):
            if remove in lista_todo:
                lista_todo.remove(remove)

lista_todo = []

while True:
    menu = int(input("O que deseja?\n1: Adicionar uma tarefa\n2: Remover uma tarefa\n3: Sair\n"))

    if menu == 1:
        todo = input("Qual tarefa você quer adicionar?? ")
        todo = todo.title()
        lista_todo.append(todo)
        view('LISTA ATUAL')

    if menu == 2:
        ler()
        remover()


    if menu == 3:
        archive()
        print('LISTA DE TAREFAS'.center(50, '-'))
        ler()
        break


def update():
    with open('proj/tarefas.txt', 'a+', encoding='utf-8') as arquivo:
        arquivo.seek(0)
        leitura = arquivo.read()
        lista_todo = [leitura]
        print(lista_todo)
update()
# O código não está funcionando na condicional 2; Deve-se utilizar a todo_list como uma LISTA:
"""
lista = ['Leonardo', 'Lucas']
a = 'Leonardo'
for i in lista:
    if a in lista:
        lista.remove(a)
print(lista)
"""