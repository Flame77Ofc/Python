# Faça um programa que verifique se uma letra digitada é vogal ou consoante.  
def vogal_consoante(letra):
  vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'é', 'è', 'ê', 'í', 'ì', 'î', 'i', 'o', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'u']
  if len(letra) > 1 or len(letra) < 1:
    return 'Por favor, digite uma letra válida'
  else:
    if letra.lower() in vogais:
      return f'Sua letra é vogal'
    else:
      return f'Sua letra é consoante'
print(vogal_consoante('w'))
print(vogal_consoante('a'))
print(vogal_consoante('ó'))
print(vogal_consoante('ty'))
