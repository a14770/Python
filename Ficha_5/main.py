from ficha5_ex1 import add, update_final_prince, print_product, menu
import os


products = []
escolha = menu()

while True:
    match (escolha):
        case 1:
            print("\n***************Novo Produto********************\n")
            prd = input("Produtos: ")
            pri = input("Preço")
            iva = input("Iva")
            products.append(add(prd,float(pri),float(iva)))
        case 2:
            for product in products:
                if "fina_price" not  in products.keys():
                    update_final_prince(product)
                print(print_product(product))    
            x = input("Prima uma tecla para continuar ...")
        case 3:
            for product in products:
                update_final_prince(product)
            x = input("Prima um tecla para continuar ...")
        case 4:
            encontrei = False
            pesquisa = input("Produto a Listar")
            for p in products:
                if p["product"] == pesquisa:
                    encontrei = True
            if not encontrei:
                print("Este produto não faz parte da LIsta")

            x = input("Prima uma tecla para continuar ...")
        case 5:
            break
    os.system("cls")    
    escolha = menu()
                                                              