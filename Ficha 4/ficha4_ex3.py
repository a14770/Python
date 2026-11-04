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
biblioteca["livro4"] = {        
    "titulo": "Doce da avó",
    "autor": "Giovani Trindade",
    "ano": 2010,
    "disponivel": True
}
print(biblioteca)

#Marca o livro 1 como nao disponivel
biblioteca["livro1"]["disponivel"] = False

#Retorna uma lista com os titulos do autor Luciano Ramalho
livrosL = []
for livro in biblioteca.values():
    if livro["autor"] == "Luciano Ramalho":
        livrosL.append(livro["titulo"])
print(livrosL)

