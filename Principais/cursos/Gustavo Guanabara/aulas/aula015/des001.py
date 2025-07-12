import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('Deu erro')
else:
    print('Site acessado com sucesso')
    print(site.read())