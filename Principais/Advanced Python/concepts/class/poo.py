'''
class Animal:
    def __init__(self, nome, altura, cor):
        self.nome = nome
        self.altura = altura
        self.cor = cor


class Gato(Animal):
    def miar(self):
        return f"{self.nome} miou!"


mia: Gato = Gato("Mia", 0.56, "Laranja")
print(mia.miar())
'''

'''
class Pessoa:
    def __init__(self, nome: str, idade: int, genero: str):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def prazer(self):
        return f"Prazer, {self.nome}!"

    def __str__(self):
        return f"nome: {self.nome}, idade: {self.idade}, genero: {self.genero}"


p1 = Pessoa("Gabriel", 15, "Masculino")
print(p1)
print(p1.prazer())
'''

'''
class Automovel:
    def __init__(self, tipo: str, modelo: str, cor: str):
        self.tipo = tipo
        self.modelo = modelo
        self.cor = cor


class Carro(Automovel):
    def dirigir(self):
        return f"O {self.tipo} {self.modelo} está dirigindo"


carro001 = Carro("Carro", "Honda", "Prata")
print(carro001.dirigir())


class Barco(Automovel):
    def navegar(self):
        return f"O {self.tipo} {self.modelo} está navegando"


barco001 = Barco("Barco", "Vela", "Marrom")
print(barco001.navegar())


class Caminhao(Automovel):
    def __init__(self, tipo: str, modelo: str, cor: str, material):
        super().__init__(tipo, modelo, cor)
        self.material = material

    def transportar(self):
        return f"O Caminhão {self.modelo} está transportando {self.material}"


caminhao001 = Caminhao("Caminhão", "Rosfargex", "Vermelho", "Madeira")
print(caminhao001.transportar())
'''

'''
class AnimalInseto:
    def __init__(self, tipo: str, cor: str, comida: str, bebida: str,
                 pernas: int, idade: int, genero: str, peso: float,
                 altura: float):
        self.tipo = tipo
        self.cor = cor
        self.comida = comida
        self.bebida = bebida
        self.pernas = pernas
        self.idade = idade
        self.genero = genero
        self.peso = peso
        self.altura = altura

    def comer(self):
        return f"{self.tipo} está comendo {self.comida}"

    def dormir(self):
        return f"{self.tipo} está dormindo"

    def beber(self):
        return f"{self.tipo} está bebendo {self.bebida}"


class Gato(AnimalInseto):
    def arranhar(self):
        return f"Hahahahaha! {self.tipo} arranhou o sofá!"


wenix = Gato("Gato", "Laranja", "Ração de Gato",
             "Leite e Água", 4, 5, "Macho", 4.5, 35)
print(wenix.arranhar())
print(wenix.comer())
print(wenix.dormir())
print(wenix.beber())

'''

'''
class Residencia:
    def __init__(self, tipo: str, cor: str, material: str,
                 area: int, quartos: int, banheiros: int, pet: bool):
        """
        tipo: str = Tipo da Residência. Ex: Prédio, Casa, Condominio, ...
        cor: str = Cor externa da residência. Ex: Verde, azul, branca, ...
        material: str = Material externo PRINCIPAL da residência. Ex: Madeira
        area: int = Área em metros quadrados da residência
        quartos: int = Quantidade de quartos que a residência possui
        banheiros: int = Quantidade de banheiros que a residência possui
        pet: bool = Valor que determina se na residência existe pet
        """

        self.tipo = tipo
        self.cor = cor
        self.material = material
        self.area = area
        self.quartos = quartos
        self.banheiros = banheiros
        self.pet = pet

    def passear_com_pet(self, lugar: str) -> str:
        """
        A função verifica se na residência existe pet e retorna uma mensagem
        """

        if self.pet:
            return f"Passeando com o pet no/na/em {lugar}"
        else:
            return "Você não tem um pet e não pode passear com o pet."

    def dormir(self, pessoa: str) -> str:
        """
        A função retorna uma mensagem da pessoa dormindo.
        """

        return f"{pessoa} está dormindo..."

    def comer(self, pessoa: str, comida: str) -> str:
        """
        A função retorna uma mensagem da pessoa comendo uma comida.
        """

        return f"{pessoa} está comendo {comida.lower()}"

    def beber(self, pessoa: str, bebida: str) -> str:
        """
        A função retorna uma mensagem de uma pessoa bebendo.
        """

        return f"{pessoa} está bebendo {bebida.lower()}"

    def sair(self, pessoas: list, destino: str) -> str:
        """
        A função retorna uma mensagem com as pessoas e o destino para onde vão.
        """

        quant_pessoas = len(pessoas)
        return (f"{', '.join(pessoas)} ({quant_pessoas} pessoas) "
                f"estão indo para {destino}")


class Casa(Residencia):
    def __init__(self, tipo: str, cor: str, material: str, area: int,
                 quartos: int, banheiros: int, pet: bool, jardim: bool,
                 garagem: bool):
        super().__init__(tipo, cor, material, area, quartos, banheiros, pet)
        """
        jardim: bool = Valor que determina se na casa existe jardim.
        garagem: bool = Valor que determina se na casa existe garagem.
        """

        self.jardim = jardim
        self.garagem = garagem

    def pintar_exterior(self, lugar: str, cor: str, area: int):
        """
        A função verifica se a casa pode ser pintada no exterior.
        Retorna uma mensagem dependendo da condição satisfeita.
        """

        if cor == self.cor:
            return f"Sua casa já está pintada de {self.cor}."
        elif area > self.area:
            return "A área ultrapassa os limites da área da casa."
        else:
            return (f"A sua casa foi pintada de {cor} na/no {lugar} "
                    f"numa área de {area}km²")

    def pintar_interior(self, lugar: str, cor: str, area: int):
        """
        A função verifica se a casa pode ser pintada no interior.
        Retorna uma mensagem dependendo da condição satisfeita.
        """

        if area > self.area:
            return "A área ultrapassa os limites da área da casa."
        else:
            return (f"A sua casa foi pintada de {cor} na/no {lugar} "
                    f"numa área de {area}km²")


casa001 = Casa("Casa", "Azul e Branco", "Quartzo", 560, 4, 3, True, True, True)
print(casa001.pintar_interior("Quarto", "Azul marinho", 45))
print(casa001.passear_com_pet("Parque"))


class Apartamento(Residencia):
    def __init__(self, tipo: str, cor: str, material: str,
                 area: int, quartos: int, banheiros: int, pet: bool,
                 sacada: bool, churrasqueira: bool):
        super().__init__(tipo, cor, material, area,
                         quartos, banheiros, pet)
        """
        sacada: bool = Valor que determina se exite sacada.
        churrasqueira: bool = Valor que determina se existe churrasqueira.
        """
        self.sacada = sacada
        self.churrasqueira = churrasqueira

    def pintar_interior(self, lugar: str, cor: str, area: int):
        """
        A função verifica se o apartamento pode ser pintado no interior.
        Retorna uma mensagem dependendo da condição satisfeita.
        """

        if area > self.area:
            return "A área ultrapassa os limites da área do apartamento."
        else:
            return (f"O seu apartamento foi pintado de {cor} na/no {lugar} "
                    f"numa área de {area}km²")


apartamento001 = Apartamento("Apartamento", "Cinza claro com Cinza escuro",
                             "Concreto", 150, 3, 1, False, True, True)
print(apartamento001.sair(["Maria", "Lucas", "Felipe"], "Disney"))
print(apartamento001.comer("Fernando", "Macarrão com carne moída"))
'''

'''
class Quadra:
    def __init__(self, largura: int, comprimento: int, jogadores: int):
        """
        largura: int = Largura da quadra em metros.
        comprimento: int = Comprimento da quadra em metros.
        jogadores: int = Quantidade de jogadores dentro de quadra.
        """

        self.largura = largura
        self.comprimento = comprimento
        self.jogadores = jogadores

        self.area = largura * comprimento


class Futebol(Quadra):
    def __init__(self, largura: int, comprimento: int, jogadores: int,
                 gols_time1: int, gols_time2: int):
        """
        gols_time1: int = Quantidade de gols do time 1.
        gols_time2: int = Quantidade de gols do time 2.
        """

        super().__init__(largura, comprimento, jogadores)
        self.gols_time1 = gols_time1
        self.gols_time2 = gols_time2

        self.gols = gols_time1 + gols_time2

    def fazer_gol(self, jogador: str):
        """
        Função que retorna uma mensagem do jogador que fez o gol.
        """

        return f"Goooooooooooooooooooooool!!! Dele dele dele dele, {jogador}!!"

    def driblar(self, jogador: str, pessoa: str, drible: str):
        """
        Função que retorna o jogador que fez o dribe, a pessoa que foi
        driblada e qual foi o drible.
        """

        return f"{jogador} driblou {pessoa} com o drible \"{drible}\""

    def chutar_bola(self, jogador: str, lugar: str):
        """
        Função que retorna o jogador que chutou a bola e em qual lugar.
        """

        return f"{jogador} chutou a bola na/no/em {lugar}"

    def placar(self):
        """
        Função que retorna o placar do time 1 e do time 2.
        """

        yield f"{self.gols_time1} gols para o time 1"
        yield f"{self.gols_time2} gols para o time 2"


futebol001 = Futebol(150, 80, 12, 2, 3)
print(futebol001.fazer_gol("Roberto Mirim"))
print(futebol001.driblar("Felipe", "Mario", "Caneta"))
print(futebol001.chutar_bola("Felipe", "Trave"))

for item in futebol001.placar():
    print(item)
'''

'''
from random import randint
from time import sleep


class Fabrica:
    def __init__(self, nome_da_fabrica: str, produto: str, materiais: list,
                 cores: list, maquinas: int):
        self.nome_da_fabrica = nome_da_fabrica
        self.produto = produto
        self.materiais = materiais
        self.cores = cores
        self.maquinas = maquinas


class Petroleo(Fabrica):
    def __init__(self, nome_da_fabrica: str, produto: str, materiais: list,
                 cores: list, maquinas: int):
        super().__init__(nome_da_fabrica, produto, materiais, cores, maquinas)

    def cavar(self, profundidade: float):
        return f"Cavando a uma profundidade de {profundidade} metros."

    def encontrar_petroleo(self, local: str):
        if randint(0, 1):
            return (f"A máquina encontrou petróleo no/em/na {local}!")
        else:
            return "A máquina não encontrou petróleo neste local."


maquina001 = Petroleo("Petrouro", "Petróleo", ["Petróleo"],
                      ["Preto", "Cinza Escuro"], 24)
print(maquina001.cavar(15))


class Bonecas(Fabrica):
    def __init__(self, nome_da_fabrica: str, produto: str, materiais: list,
                 cores: list, maquinas: int, bonecas_produzidas_por_dia: int):
        super().__init__(nome_da_fabrica, produto, materiais, cores, maquinas)
        self.bonecas_por_dia = bonecas_produzidas_por_dia

    def fazer_boneca(self, cor_de_pele: str, altura: float):
        yield f"Preparando boneca {cor_de_pele} com {altura}cm. Aguarde..."
        sleep(15)

        yield f"Boneca {cor_de_pele} com {altura}cm produzida."


bonecas001 = Bonecas("Doll Maker", "Bonecas",
                     ["Plástico", "Tecido de Roupa", "Tintas"],
                     ["Branco", "Bege", "Moreno"], 28, 21600)
# for item in bonecas001.fazer_boneca("branca", 68):
#     print(item)
'''

'''
class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int, descricao: str,
                 nota: int):
        """
        titulo: str = Título do livro.
        autor: str = Autor do livro, quem escreveu o livro.
        descrição: str = Descrição do livro, resumo geral e detalhado.
        nota: int = Nota de 1 a 10 para o livro.
        paginas: int = Quantidade de páginas que o livro possui.
        """

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.descricao = descricao
        self.nota = nota

    def ler_livro(self, pagina: int):
        if pagina <= self.paginas:
            yield f'Lendo "{self.titulo}" na página {pagina}.'
            yield "Muito interessante!"
        else:
            yield f"Ooops! A página deve ser menor que {self.paginas}."


livro001 = Livro("O grande Livro do Manual do Mundo de matemática",
                 "Iberê Thenório", 525,
                 "recomendo este livro para os amantes da matemática. "
                 "Este livro ensina os tópicos essenciais até os mais "
                 "avançados, começando com juros, descontos, taxas, frações e "
                 "indo para equações de 1o/2o Grau, etc...", 10)
for item in livro001.ler_livro(525):
    print(item)
'''

'''
class Funcionario:
    def __init__(self, loja: str, nome: str, idade: str, salario: int,
                 saldo: int):
        self.loja = loja
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.saldo = saldo

    def trabalhar(self, acao: str):
        return f"{self.nome} está {acao}."

    def ganhar_dinheiro(self, quantidade: int):
        self.saldo += quantidade
        return f"{self.nome} ganhou R${quantidade}."

    def ver_saldo(self, banco: str):
        return f"Saldo atual do {banco} de {self.nome}: {self.saldo}"


func001 = Funcionario("McDonald's", "Lucas", 25, 4550, 34500)
print(func001.trabalhar("fazendo batatas-fritas"))

func002 = Funcionario("Magazine Luiza", "Maria", 37, 3250, 67325)
print(func002.trabalhar("entregando encomendas"))
print(func002.ganhar_dinheiro(3250))
print(func002.ver_saldo("Nubank"))
'''

'''
class Celular:
    def __init__(self, marca: str, modelo: str, aplicativos: int):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self) -> str:
        if not self.ligado:
            self.ligado = True
            return "Celular ligado."
        else:
            return "Celular já está ligado."

    def desligar(self) -> str:
        if self.ligado:
            self.ligado = False
            return "Celular desligado."
        else:
            return "Celular já está desligado."

    def abrir_aplicativo(self, aplicativo: str):
        if self.ligado:
            return f'Abrindo o app "{aplicativo}"...'
        else:
            return "Por favor, primeiro ligue o celular."

    def navegador(self, nome_do_site: str, nome_do_navegador: str) -> bool:
        if self.ligado:
            return f'Acessando "{nome_do_site}" em {nome_do_navegador}...'
        else:
            return "Por favor, primeiro ligue o celular."


Samsung001 = Celular("Samsung", "M52", 56)
Samsung001.ligar()
print(Samsung001.navegador("google", "Tor Browser"))

Xiaomi001 = Celular("Xiaomi", "12S", 102)
Xiaomi001.ligar()
print(Xiaomi001.abrir_aplicativo("Duolingo"))
Xiaomi001.desligar()
'''

'''
class Biblioteca:
    def __init__(self, nome_pessoa: str, livro: str, paginas_livro: int,
                 preco_livro: float):
        """
        nome_pessoa: str = Nome da pessoa que tem o livro.
        livro: str = Nome do livro.
        paginas_livro: int = Quantidade de páginas que o livro possui.
        preco_livro: float = Preço do livro.
        """

        self.nome = nome_pessoa
        self.livro = livro
        self.paginas = paginas_livro
        self.preco = preco_livro

    def comprar_livro(self):
        """
        Função responsável por carregar os dados do objeto dentro de um
        arquivo.
        """

        with open("biblioteca.txt", "a+", encoding="utf-8") as biblioteca:
            biblioteca.seek(0)
            conteudo = biblioteca.read()

            if self.nome not in conteudo or self.livro not in conteudo:
                with open("biblioteca.txt", "a",
                          encoding="utf-8") as biblioteca:

                    biblioteca.write(f"Pessoa: {self.nome}\nLivro: "
                                     f"{self.livro}"
                                     f"\nPreço: {self.preco}\n\n")

                return "Livro comprado com sucesso."
            else:
                return "Usuário já cadastrado."


Lucas = Biblioteca("Lucas", "Hábitos Atômicos", 450, 45.99)
print(Lucas.comprar_livro())

Maria = Biblioteca("Maria", "O Guia COMPLETO de Python", 980, 159.99)
print(Maria.comprar_livro())

Roberto = Biblioteca("Roberto", "O Guia COMPLETO de Python", 980, 159.99)
print(Roberto.comprar_livro())
'''

'''
from time import sleep


class Delivery:
    def __init__(self, endereco: str, cliente: str, lanche: str,
                 entregador: str, demora: int):
        self.endereco = endereco
        self.cliente = cliente
        self.lanche = lanche
        self.entregador = entregador
        self.demora = demora

        self.pedido = False

    def pedir_lanche(self) -> str:
        self.pedido = True
        return (f"{self.entregador} está a caminho. "
                f"Indo para {self.endereco}...")

    def receber_lanche(self):
        if self.pedido:
            sleep(5)
            return f"Toc Toc Toc! Seu {self.lanche} está na sua porta!"
        else:
            return "Você precisa primeiro pedir o seu lanche!"


lanche001 = Delivery("Rua Coca-Cola", "Lucas", "X-Salada",
                     "Alberto Josvaldo", 15)
print(lanche001.pedir_lanche())
print(lanche001.receber_lanche())

lanche002 = Delivery("Rua dos Astronautas", "Felipe dos Santos", "Hot Dog",
                     "Cleusa Roberta", 12)
print(lanche002.pedir_lanche())
print(lanche002.receber_lanche())
'''

'''
class Email:
    def __init__(self, nome_email: str, usuario: str,
                 criptografado: bool, ilimitado: bool):
        """
        nome_email: str = Define o nome do software do email. Ex:
        Gmail, Proton Mail.

        usuario: str = Define o nome de usuário da pessoa.

        criptografado: bool = Define se o software do email é criptografado.
        Isso é, se possui criptografia entre mensagens.

        ilimitado: bool = Define se o software do email é ilimitado.
        Isso é, se é possível enviar mensagens ilimitadas - Sem assinatura.
        """

        self.nome_email = nome_email
        self.usuario = usuario
        self.criptografado = criptografado
        self.ilimitado = ilimitado

    def enviar_mensagem(self, destinatario: str, mensagem: str) -> str:
        """
        Função que simula o envio de uma mensagem pelo email.

        destinatario: str = Define o nome de usuário da pessoa que recebe
        a mensagem.

        mensagem: str = Mensagem que será enviada para o destinatario.
        """

        return f"Você enviou uma mensagem para {destinatario}."

    def ver_email(self):
        """
        Função que simula a visualização da caixa de entrada do email.
        Retorna "Nenhuma mensagem".
        """

        return "Nenhuma mensagem :("


email001 = Email("Proton Mail", "Flame77OFC", True, False)
print(email001.enviar_mensagem("Snowzin078", "Olá!"))
'''

'''
class Musica:
    def __init__(self, nome_da_musica: str, artista: str, duracao: str):
        """
        nome_da_musica: str = Nome da música.

        artista: str = Artista que criou a música.

        duracao: str = Duração da música no formato mm:ss.
        mm = minutos; ss = segundos. Ex: 02:12
        """

        self.musica = nome_da_musica
        self.artista = artista
        self.duracao = duracao

    def tocar_musica(self):
        return f"Tocando agora: {self.musica} de {self.artista}!"

    def avaliar_musica(self, avaliacao: str):
        return f"Você avaliou: {avaliacao}"

    def compartilhar_musica(self, pessoas: list):
        return f"Você compartilhou {self.musica} para {', '.join(pessoas)}"


guanabara_hits = Musica("Guanabara Hits", "Gustavo Guanabara", "2:45")
print(guanabara_hits.tocar_musica())
print(guanabara_hits.avaliar_musica("Muito boa!! Feita pelo nosso mestre!!!"))
print(guanabara_hits.compartilhar_musica([
    "João", "Maria", "Felipe", "José", "Claúdia", "Matheus", "Tiago"
]))

after_dark = Musica("After Dark", "Mr. Kitty", "04:26")
print(after_dark.tocar_musica())
print(after_dark.avaliar_musica("Dark Vibes!🎃"))
print(after_dark.compartilhar_musica([
    "Sidney", "Wevertson", "Lucas", "Fernando", "Gabriel", "Bernardo"
]))
'''

'''
import requests
from bs4 import BeautifulSoup


def get_valor_dolar():
    try:
        r = requests.Session().get(
            "https://search.brave.com/search?q=cotacao+dolar&source=newtab"
        )

        soup = BeautifulSoup(r.content, 'html.parser')

        dolar = float(soup.find('span', attrs={
            'class': 'amount t-primary svelte-14vyw89'
        }).getText().strip().replace(",", "."))

        return dolar
    except Exception as erro:
        print(f"Não foi possível capturar o valor do dolar. Erro: {erro}")
        return None


class Moeda:
    def __init__(self, quantidade: float):
        self.quantidade = quantidade

    def converter_para_dolar(self):
        dolar = get_valor_dolar()

        if dolar:
            return (
                f"O valor do dólar hoje é {dolar}\n"
                f"{dolar} x {self.quantidade} = {dolar * self.quantidade}"
            )


moeda = Moeda(45)
print(moeda.converter_para_dolar())
'''
