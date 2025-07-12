import random

tamanho = int(input("Digite o tamanho da senha (senha < 83): "))
criptografia = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()%-_=+-&*?"

senha = "".join(random.sample(criptografia, tamanho))
print(senha)
