# Encontrar a palavra mais longa de uma string
def find_longest_word(string: str):
    if len(string) < 1 or len(string) > 250:
        return "O tamanho da string deve estar entre 1 a 250."

    spplited_string = string.split()
    lenghts_list = list(map(len, spplited_string))
    biggest_lenght = lenghts_list.index(max(lenghts_list))
    longest_word = spplited_string[biggest_lenght]

    return longest_word


if __name__ == "__main__":
    print(find_longest_word("Python ou JavaScript?"))  # JavaScript?
    print(find_longest_word("Essa aqui é a maior palavra"))  # palavra
    print(find_longest_word("lorem ipsum dolor"))  # lorem (encontra a primeira palavra com maior tamanho)
