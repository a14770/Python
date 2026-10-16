from random import randint
import os

resposta = "S"

while resposta == "S":
    tentativa = 0
    numGerado = randint(1, 100)
    pontuacao = 0
    pontuacoes = [10, 20, 30, 40, 50, 60, 80, 90, 100]
    print(numGerado)

    while tentativa < 7:
        meuNumero = int(input("Tente gerar um novo valor: "))
        while meuNumero < 1 or meuNumero > 100:
            print("Valor invalido! O valo de ser entre 1 a 100: ")
            meuNumero = int(input("Tente novamente betinha kkkj: "))
        os.system("clear")
        tentativa = tentativa + 1
        if meuNumero == numGerado:
            print(f"Parabens acerto o numero kkkj: ")
            break
        if meuNumero > numGerado:
            print("Tente de novo - dica o valor e menor: ")
        else:
            print("Tente de novo - dica o valor e maior. ")
    if tentativa == 7:
        print(f"Voce nao acerto kkk {numGerado}: ")

    pontuacao = pontuacoes[tentativa - 1]
    print(f"Pontuacao: {pontuacao}") 

    resposta = input("Deja jogar novamente (S|N): ").upper()
