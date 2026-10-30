#Exercicio 1 1: Criação e Manipulação Básica

aluno = {

 "nome": "Ana Silva",
 "idade": 17,
 "Diciplina": ["Matematica", "Fisica","Informatica"],
 "notas":{"Matematica":18,"Fisica":17, "Informatica":19}
 }

#1 Adicionar uma nova diciplina
aluno["Diciplina"].append("Educação Fisica ")

#2 Modificar idade
aluno["idade"] = 18

#3 Imprimar toas as diciplinas e notas
for diciplina, nota in aluno["notas"].items():
    print(f"{diciplina}: {nota}")

#4 Calcule e imprima a media das notas
soma = sum(aluno["notas"].values())
media = soma / len(aluno["notas"])
print(f"A media e : {media}")

print("Nome:",aluno["nome"])
print("idade:",aluno["idade"])
print("Diciplina:",aluno["Diciplina"])
print("notas:",aluno["notas"])






