from random import randint

lista = []
x = 0

pares = 0
impar = 0  
maior = 0
menor = 101  
soma = 0

for _ in range(30):
    x = randint(1, 100)
    lista.append(x)

for num in lista:

    if num % 2 == 0:
        pares = pares + 1
    else:
        impar = impar + 1  
  
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    soma = soma + num
media = soma / 30

superiores_media = []
for num in lista:
    if num > media:
        superiores_media.append(num)

quantidade_superiores = len(superiores_media)



print("Lista completa:", lista)
print("Numeros Pares:", pares)
print("Numeros Impar:", impar)
print("O maior número:", maior) 
print("O menor número:", menor) 
print("Media Lista:", media)
print("Numeros maior que a media:", quantidade_superiores) 
print("Números superiores à média:", superiores_media)  