produtos = []

def add (produto, preco, iva=0.23):
    return {
        "product": produto,
        "preco": preco,
        "iva": iva,
    }

def update_final_prince(d):
    d("final_preco") = round (d["preco"] * (1 + d ["iva"],2))

def print_product(d):
    return f"= O produto {d["product"]} com preço de {d["preco"]} e iva de {d["iva"]*100}%"


def menu():
    print("1 - Inserir lista de Produto")
    print("2 - Listar os produtos existentes")
    print("3 - Atualizar o preco final de todos os produtos existente")
    print("4 - Imprimir os dados de um produto especifico")
    print("5 - Terminar a aplicaçao")
    op = int(input("\nEscolha a opeção"))
    return op