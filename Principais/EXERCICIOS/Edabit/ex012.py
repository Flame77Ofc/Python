"""Smith criou uma loja de produtos e-commerce. Ele tem uma conta especial para ele mesmo, com mais de 100 mil clientes em sua loja. Ele precisa que você crie uma função que retorne uma mensagem agradável se a senha for a de Smith."""

def loja(senha):
    if senha == 'Smith1234':
        return 'Olá, Smith!'
    else:
        return 'Olá, usuário!'
print(loja('Smith1234'))
print(loja('passeord0998'))