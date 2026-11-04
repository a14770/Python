# 1. Crie um dicionário onde as chaves são números de 1 a 10 e os valores são os quadrados desses números.

quadrados = {str(i): i*i for i in range(1,11)}
print(quadrados)

# 2. A partir de uma lista de palavras, crie um dicionário onde as chaves são as palavras e os valores
# são os comprimentos dessas palavras.
palavras = ["Alicate","Dados","Parlamento","Python","Dicionario"]
dic_palavras = {palavra: len(palavra) for palavra in palavras}
print(dic_palavras)

# 3. A partir do dicionário notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12,"Eva": 19} ,
# crie um novo dicionário que contenha apenas os alunos com notas superiores ou iguais a 15.
notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12,"Eva": 19}
melhores_alunos = {aluno: nota for aluno,nota in notas.items() if nota >= 15}





quadrados = {str(i): i*i for i in range(1,11)}
print(quadrados)


palavras = ["Alicate","Dados","Parlamento","Python","Dicionario"]
dic_palavras = {palavra: len(palavra) for palavra in palavras}
print(dic_palavras)


notas = {"Ana": 18, "Bruno": 15, "Carla": 17, "David": 12, "Eva": 19}
melhores_alunos = {aluno: nota for aluno, nota in notas.items() if nota >= 15}