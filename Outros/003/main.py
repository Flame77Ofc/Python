loged_user = False
if loged_user:
    msg = 'Olá'
else:
    msg = 'Precisa logar'
print(msg)

msg = 'Olá' if (loged_user) else 'Precisa logar'
print(msg)