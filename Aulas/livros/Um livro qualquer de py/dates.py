import datetime
ano = datetime.datetime.now().year
mes = datetime.datetime.now().month
dia = datetime.datetime.now().day
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
segundo = datetime.datetime.now().second
microsegundo = datetime.datetime.now().microsecond

# datetime: Ano, mês, dia e opcional horas, minutos, segundos, microssegundos
y = datetime.datetime(2025, 5, 4)
print(y)

# time: horas, minutos, segundos, microssegundos
x = datetime.time(12, 30, 00)
print(x)


# timedelta
tdelta = datetime.timedelta(days=1)
print(tdelta)



# exemplo
agora = datetime.datetime.now()
horario_cinema = datetime.datetime(2025, 5, 4, 12)
horario_restante = horario_cinema - agora

print(horario_restante)


import datetime
data = datetime.datetime.now()
print(data)

amanha = datetime.datetime.now().day + 1
print(amanha)



ano_posterior = datetime.datetime.now().year + 1
print(ano_posterior)



data_especifica = datetime.datetime(year=2050, month=9, day=1, hour=12, minute=30, second=35, microsecond=900000)
print(data_especifica)


# formatando
data = "01/09/2026"
data = datetime.datetime.strptime(data, "%d/%m/%Y")
print(data)

# formatando na data brasileira
print(data.strftime("%d/%m/%Y"))

import datetime
x = datetime.datetime.now()
print(x)

# pode ser acessado o ano/mes/dia/semana/hora/minuto/segundo/microsegundo desses dois jeitos:
"x = datetime.datetime.now().year"
print(x.year)


# formatando para a data brasileira
x = datetime.datetime.now()
x = x.strftime("%d/%m/%Y")
print(x)


# criando suas próprias datas:
"datetime.datetime(<obrigatório>, <opcional>) obrigatório: ano, mês, dia; opcional: hora, minuto, segundo, microsegundo"
x = datetime.datetime(2025, 5, 12) # Não pode haver 0 antes do mês/dia.
print(x)


import datetime
# Imprime ano, mês e dia, hora, minuto, segundo e microsegundo.
agora = datetime.datetime.now()
print("Data e hora atuais:", agora)

# Imprime ano, mês e dia
hoje = datetime.date.today()
print("Data de hoje:", hoje)

# Criando um objeto datetime específico
data_especifica = datetime.datetime(2025, 5, 3, 14, 30, 0)
print("Data específica:", data_especifica)

# Criando apenas um objeto date
data_apenas = datetime.date(2025, 5, 3)
print("Apenas a data:", data_apenas)

# Criando apenas um objeto time
hora_apenas = datetime.time(14, 30, 0)
print("Apenas a hora:", hora_apenas)

# Diferença entre datas (timedelta)
data_futura = hoje + datetime.timedelta(days=10)
print("Data daqui a 10 dias:", data_futura)


# Formatando datas (strftime)
formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", formatado)

# Transformando string em datetime (strptime)
data_str = "03/05/2025 14:30:00"
data_convertida = datetime.datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("String convertida em datetime:", data_convertida)