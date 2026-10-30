#1: Exercício 2: Contagem de Frequência

nome = "Programacao"

contagem = {}
for letra in nome:
    if letra in contagem.keys():
        contagem[letra] += 1 
    else:
        contagem[letra] = 1
print(contagem)