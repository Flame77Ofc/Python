# Crie uma função que recebe um número de 1 a 12 e retorna o nome do mês correspondente como uma string.
meses_string = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def retorna_mes(mes_int):
  return 'Não foi possível acessar.' if mes_int < 0 or mes_int > 12 else meses_string[mes_int-1]
print(retorna_mes(6))
print(retorna_mes(12))
print(retorna_mes(3))
