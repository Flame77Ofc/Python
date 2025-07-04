# Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para validar o seu acesso ao sistema. Considere que a senha ficticia do correntista é 123456. Considere as seguintes restrições:
# quando a senha estiver correta, mostrar a mensagem: "Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
# quando o usuário errar a senha pela primeira vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 2 tentativas."
# se o usuário errar a senha pela segunda vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 1 tentativa."
# se o usuário errar a senha novamente, mostrar a mensagem "Sua senha foi bloqueada Por favor, dirija-se a um de nossos caixas." e o programa deve ser encerrado.

nome = input('Digite o seu nome: ').strip().title()
tentativas = 3
while tentativas >= 1:
  senha = int(input('Digite a sua senha: '))
  if senha == 123456:
    print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
    break
  else:
    if tentativas == 1:
      print("Sua senha foi bloqueada. Por favor, dirija-se a um de nossos caixas.")
      break
    else:
      tentativas -= 1
      print(f'Senha incorreta! Você ainda tem {tentativas} tentativas.')
