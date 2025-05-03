def carregar_contas():
    contas = {}
    try:
        with open("contas.txt", "r") as f:
            for linha in f:
                nome, senha, saldo = linha.strip().split(",")
                contas[nome] = {"senha": senha, "saldo": int(saldo)}
    except FileNotFoundError:
        pass  # Se o arquivo não existir ainda
    return contas

def salvar_contas(contas):
    with open("contas.txt", "w") as f:
        for nome, dados in contas.items():
            f.write(f"{nome},{dados['senha']},{dados['saldo']}\n")

def criar_conta(contas):
    nome = input("Nome de usuário: ")
    if nome in contas:
        print("Usuário já existe!")
        return
    senha = input("Senha: ")
    contas[nome] = {"senha": senha, "saldo": 0}
    salvar_contas(contas)
    print("Conta criada com sucesso!")

def login(contas):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome in contas and contas[nome]["senha"] == senha:
        print(f"Bem-vindo, {nome}!")
        return nome
    else:
        print("Usuário ou senha incorretos!")
        return None

def menu_usuario(contas, nome):
    while True:
        print(f"\nSaldo: R${contas[nome]['saldo']}")
        print("1: Depositar")
        print("2: Sacar")
        print("3: Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            valor = int(input("Quanto quer depositar? "))
            contas[nome]['saldo'] += valor
        elif opcao == '2':
            valor = int(input("Quanto quer sacar? "))
            if valor <= contas[nome]['saldo']:
                contas[nome]['saldo'] -= valor
            else:
                print("Saldo insuficiente!")
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")
        salvar_contas(contas)

def main():
    contas = carregar_contas()
    while True:
        print("\n1: Criar conta\n2: Login\n3: Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_conta(contas)
        elif opcao == '2':
            nome = login(contas)
            if nome:
                menu_usuario(contas, nome)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()