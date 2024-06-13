import os
os.system("cls || clear")

class livros:
    def __init__(self, titulo, autor, numero_de_paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.preco = preco

QUANTIDADE_LIVROS = 2
livros = []

for i in range(QUANTIDADE_LIVROS):
    titulo = input("Digite seu titulo: ")
    autor = input("Digite o autor: ")
    numero_de_paginas = input("Número de pagina: ")
    preco = float(input("Digite o preço: ")) 
    livro = livros(titulo, autor, numero_de_paginas, preco)
    livros.append(livro)

for i in livros:
        print(f"\nTitulo do livro: {i.titulo}")
        print(f"Nome do autor: {i.autor}")
        print(f"Numero de paginas: {i.numero_de_pagina}")
        print(f"O preço do livro: {i.preco}")