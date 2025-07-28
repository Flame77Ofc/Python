import random

def criptografar_senha(tamanho: int):
    if tamanho >= 83 or tamanho < 8:
        return "Tamanho inválido. O tamanho deve ser entre 8 e 83 caracteres"

    criptografia = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()%-_=+-&*?"
    senha = "".join(random.sample(criptografia, tamanho))

    return f"Senha gerada com sucesso!\n{senha}"


try:
    tamanho = int(input("Digite o tamanho da senha:\n>>> "))
    print(criptografar_senha(tamanho))
except Exception as e:
    print(f"Erro: {e}")
