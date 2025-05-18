import datetime
agora = datetime.datetime.now()
cinema = datetime.datetime(2025, 5, 3, 23)
restante = cinema - agora

if agora <= cinema:
    print('O horário restante é', restante)
else:
    print('Acabou!')