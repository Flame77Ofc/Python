def count_words(text):
    splitted_text = text.split()
    already_list = []

    for element in splitted_text:
        if element not in already_list:
            already_list.append(element)
            print(f"{element}: {splitted_text.count(element)}")

if __name__ == "__main__":
    count_words("Python é a melhor linguagem! Eu amo Python!")
    count_words("JavaScript é uma linguagem usada em diferentes situações. é uma linguagem muito legal")
