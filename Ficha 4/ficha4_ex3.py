biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}


#1: Imprimir os titulos de todos os livros disponiveis.

for livro in biblioteca.values():
    nome_livro = livro["titulo"]
    print("Titulo do livro",nome_livro)

#2: Adiconar um novo livro a biblioteca
biblioteca ["Livro 4"]

print (biblioteca)