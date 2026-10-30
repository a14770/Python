aluno = {"nome": "Giovani", "idade": 17, "cidade": "Famlicao", "Diciplina": ["Matematica", "Progamacao","Ingles"], "notas": {"Matematica": [10,12,20], "Progamacao": [20,20,20], "Ingles": [8,19,12]}}
print(aluno["nome"])


#Media de todas as notas
soma = 0
no_notas = 0
for notas_diciplina in aluno["notas"].values():
    soma = sum(notas_diciplina)
    no_notas += len(notas_diciplina)
    

#Alterar um valor de uma chave
aluno["idade"] = 18

#Inserir uma nova chave 
aluno["estado_civil"] = "Solteiro"
print(aluno)

#Eu quero impremir as caracteristicas do aluno
for chave in aluno.keys():
    print(chave, end= " ")

#Imprimir somente os valores de aluno
for valor in aluno.values():
    print(valor, end= " ")

#Imprimir as chabes e valores do aluno
for chave, valor in aluno.items():
    print(f"{chave, valor}", end= " ")

print(aluno["Diciplina"])

#Como adicionar numa lista de um dicionario
aluno["Diciplina"].append("Portugues")
print(aluno["Diciplina"])



