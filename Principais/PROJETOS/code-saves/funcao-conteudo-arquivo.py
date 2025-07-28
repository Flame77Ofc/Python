# Crie um programa que receba o nome de um arquivo como parâmetro e retorne o conteudo do arquivo

def ler(arquivo):
    try:
        with open (arquivo, 'r', encoding='utf-8') as arquivo:
            arquivo.seek(0)
            conteudo = arquivo.read()

        return conteudo
    except FileNotFoundError:
        return "Não foi possível encontrar o arquivo. Verifique o diretório e tente novamente."
    except Exception as e:
        return f"Erro: {e}"


print(ler('readme.md'))
