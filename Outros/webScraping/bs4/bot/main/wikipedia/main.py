assunto = input('Digite o assunto que deseja pesquisar: ').strip()

from .wikipedia import wikipedia
wikipedia(assunto)