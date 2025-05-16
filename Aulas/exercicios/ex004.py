# Problema: Você foi contratado(a) por uma empresa de e-commerce e foi solicitado a você que faça uma limpeza nos cadastros de clientes duplicados. Os cadastros dos clientes estão em uma lista e você deve gerar uma lista nova sem os valores duplicados.

cadastro = ['João', 'Felipe', 'Maria', 'Maria', 'Felipe', 'Marcio', 'Felipe', 'Tereza', 'Fabio', 'Felipe']
cadastro = set(cadastro)
print(cadastro)