import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "teclado"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    return " ".join(letra if letra in letras_corretas else "_" for letra in palavra)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\nPalavra:", exibir_palavra_oculta(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        
        tentativa = input("Digite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida! Digite apenas uma letra.")
            continue
        
        if tentativa in letras_corretas:
            print("Você já tentou essa letra!")
            continue
        
        if tentativa in palavra:
            letras_corretas.add(tentativa)
            print("Boa! A letra está na palavra.")
        else:
            tentativas -= 1
            print("Errou! Essa letra não está na palavra.")
        
        if set(palavra) == letras_corretas:
            print("\nParabéns! Você acertou a palavra:", palavra)
            return
    
    print("\nFim de jogo! Você perdeu. A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()