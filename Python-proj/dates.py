# Datetime
# Já pensou em aplicar datas e horas no seu programa? É totalmente possível fazer isso utilizando o datetime, uma biblioteca do python que te permite trabalhar com horas e datas, vamos nessa?
# A primeira coisa que se deve fazer é importar o datetime, deste jeito:
import datetime
# Pronto, após isso podemos brincar com as datas e as horas!
# Primeiramente vamos ver como acessar o ano, o mes e o dia:
ano = datetime.datetime.now().year
mes = datetime.datetime.now().month
dia = datetime.datetime.now().day
# Criamos uma variável ano e utilizando as funcionalidades do datetime, atribuímos o seu valor para o ano atual. Fizemos a mesma coisa para o mês e o dia. Isso segue um padrão: datetime.datetime.now() e logo após o now utilizamos a função que queremos em inglês, por exemplo, dia -> day; mês -> month; ano -> year

# Vamos acessar também a hora, o minuto, o segundo e até o microssegundo!
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
segundo = datetime.datetime.now().second
microsegundo = datetime.datetime.now().microsecond
# Novamente segue o mesmo padrão anteriormente já dito. Se você já sabe ano, mês, dia, hora, minuto, segundo e microssegundo em inglês, então pode facilmente entender o conceito de datas e horas utilizando o datetime. 
# Que tal criarmos nossa própria data?
# Utilizando o datetime.datetime(ano, mês, dia) podemos criar nossas próprias datas. Vamos ver um exemplo:
# datetime: Ano, mês, dia {opcional horas, minutos, segundos, microssegundos}
data = datetime.datetime(2025, 5, 4)
print(data) # 2025-05-04 00:00:00
# Não especificamos as horas, mins, segs e microsegs, vamos fazer isso:
data = datetime.datetime(2025, 5, 4, 15, 30, 00)
print(data) # 2025-05-04 15:30:00

# Agora vamos supor que queremos apenas as horas, mins e segs. Podemos criar isso utilizando o datetime.time(horas, minutos, segundos, microssegundos)
# time: horas, minutos, segundos, microssegundos
time = datetime.time(12, 30, 00)
print(time) # 12:30:00


# Também é possível utilizar matemática com datas! Vamos ver como isso funciona:
# Vamos supor que vamos ao cinema, e o cinema fecha daqui 15 minutos, considerando que agora são 13:30.
agora = datetime.datetime(2025, 5, 17, 13, 30, 00)
cinema = datetime.datetime(2025, 5, 17, 13, 45, 00)
print(cinema - agora) # 0:15:00

# Podemos fazer cálculos envolvendo anos, meses, dias, enfim, qualquer função.
amanha = datetime.datetime.now().day + 1
print(amanha)
ano_posterior = datetime.datetime.now().year + 1
print(ano_posterior)