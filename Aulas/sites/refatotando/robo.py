class Robo:
    def __init__(self, nome, cor, modelo, tamanho):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.tamanho = tamanho

    def detector_objetos(self):
        objeto = False
        if objeto:
            print(f'🔴 Bip bip bip! {self.nome} DETECTOU UM OBJETO! 🔴')
        else:
            print(f'✅ {self.nome} não detectou nenhum objeto ✅')
    
    def analisa_bitcoin(self):
        achou = True
        if achou:
            bitcoin = 3.45
            dinheiro = int(bitcoin * 330000)
            print(f"🔺 BITCOINS DETECTADOS! {bitcoin} bitcoins! dinheiro = {dinheiro} 🔺")
        else:
            bitcoin = 0
            print('Nenhum bitcoin detectado')


FLOOF = Robo('Floof', 'Branco', 'Moderno', 30)
FLOOF.detector_objetos()

BROWN = Robo('Brown', 'Cinza', 'Futuristico', 140)
BROWN.analisa_bitcoin()