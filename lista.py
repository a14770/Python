nums = [2,5,11,7,9,13]

#Imprimir a lista
print(nums) # 2,5,11,7,9,13

#Imprimir um elemneto da lista 
print(nums[2]) #11

#Inserir um novo elemento no final da lista
nums.append(17) # 2,5,11,7,9,13,17

#Inserir varios elementos no final da lista
nums.extend([12,16]) # 2,5,11,7,9,13,17,12,16

#Inserir numa posiçao especifica
nums.insert(3,29) #  2,5,11,29,7,9,13,17,12,16

# Remover um elemento do final da lista
nums.pop() #
# Remover um elemento de uma posição expesifica da lista pelo indice
nums.pop(2) #
# Remover um elemento de uma posição especifica de uma listapelo valor
nums.remove(17)
# numero de elementos 
total = len(nums)

for n in nums: #Para cada elemento da minha lista 
    if n <=10:
        print(n,end="")


for indice in range(len(nums)):
    if nums[indice] <= 10:
        print(nums[indice], end="")

soma = sum(nums)
maior = sum(nums)
menor = sum(nums)
media = soma/len(nums)