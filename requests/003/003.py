import requests

# PEGANDO TODO O CODIGO HTML DE UM SITE
site = requests.get('https://xkcd.com/353/')
print(site.ok)
print(site.text)



imagem = requests.get('https://imgs.search.brave.com/dgt_Gwc5fjXmbZWRIPoVdAyCMatBl3Jr5W-XBSrw8r8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgy/NzcxOTY1L2VzL2Zv/dG8vZ2F0by1jdXJp/b3NvLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz11dWk5NFh0/TDIxbk91azEtemVu/OEk0WERRUW9BOUp6/cExySlpQc3pGLUlJ/PQ')

with open('003/imagem.png', 'wb') as arquivo:
    arquivo.write(imagem.content)