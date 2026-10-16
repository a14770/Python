from random import randint
import os
from biblioteca import z

x = 5
print (f"O valor do x e {6}", end= "")

for _ in range(5):
    y = randint(5,12)
    print(y)

    x = y + z
    print("\nValor de x = ", x)


texto = "Color"
print(texto[0])
print(texto[1:4])
print(texto[:3])
print(texto[1:])

# Passe por cada letra de uma palavra e mediz o numero de vogais 

texto = "Giovani Trindade"
num_vogais = 0
for letra in texto:
    if letra in "aeiouAEIOU":
        num_vogais = num_vogais + 1
print (num_vogais)

