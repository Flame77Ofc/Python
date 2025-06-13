# Um quiz de perguntas, onde aparecerá perguntas e o usuário deve digitar a resposta correta. Serão 5 perguntas e cada vale 2 pontos. No final, o programa mostra o total de acertos e a porcentagem de acertos
nota = 0
acertos = 0

def geral(alt1, alt2, alt3, alt4, let1, let2, letra):
    print(f'Questão {let1}'.center(50, '-'))
    print(perguntas[let2])
    print(f'a. {alt1}\nb. {alt2}\nc. {alt3}\nd. {alt4}')
    global nota, acertos
    pergunta = input('')
    if pergunta == letra:
        print('Acertou!')
        nota += 2
        acertos += 1
    else:
        print('Errou')


perguntas = {
    1: "O que o sol é?",
    2: "Qual era um dos interesses de Nietzsche?",
    3: "Quantas luas Saturno possui?",
    4: "Aonde Leonardo Da Vinci nasceu?",
    5: "O que são hertz?"
}

# Pergunta 01
geral('Satélite Natural', 'Planeta', 'Estrela', 'Cometa', 1, 1, 'c')
# Pergunta 02
geral('Matemática', 'Filosofia', 'Física', 'Artes', 2, 2, 'b')
# Pergunta 03
geral(76, 94, 105, 274, 3, 3, 'd')
# Pergunta 04
geral('Itália', 'França', 'Alemanha', 'Inglaterra', 4, 4, 'a')
# Pergunta 05
geral('Frequência', 'Temperatura', 'Velocidade', 'Distância', 5, 5, 'a')
# Imprime as notas
print(f"Sua nota foi {nota}")
print(f"Você acertou {nota * 10}% ({acertos}/5)")
