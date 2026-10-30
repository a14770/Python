tarefas = []
copiat = []

while True:
    print()
    print("===== GESTOR DE TAREFAS =====")
    print("1  - Adicionar tarefa")
    print("2  - Adicionar várias tarefas")
    print("3  - Inserir tarefa numa posição")
    print("4  - Remover tarefa por nome")
    print("5  - Remover última tarefa ou por índice")
    print("6  - Remover todas as tarefas")
    print("7  - Contar ocorrências de uma tarefa")
    print("8  - Encontrar índice de uma tarefa")
    print("9  - Ordenar tarefas (A-Z)")
    print("10 - Inverter ordem das tarefas")
    print("11 - Copiar lista de tarefas")
    print("12 - Ver tarefas")
    print("0  - Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        tarefa = input("Nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        texto = input("Escreve as tarefas separadas por vírgula: ")
        novas = texto.split(",")
        tarefas.extend(novas)
        print("Tarefas adicionadas!")

    elif opcao == "3":
        tarefa = input("Nova tarefa: ")
        posicao = int(input("Em que posição (0 = início)? "))
        tarefas.insert(posicao, tarefa)
        print("Tarefa inserida!")

    elif opcao == "4":
        tarefa = input("Que tarefa queres remover? ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida!")
        else:
            print("Essa tarefa não existe.")

    elif opcao == "5":
        if len(tarefas) == 0:
            print("A lista está vazia.")
        else:
            indice = input("Índice a remover (deixa vazio para remover a última): ")
            if indice == "":
                removida = tarefas.pop()
            else:
                removida = tarefas.pop(int(indice))
            print("Tarefa removida:", removida)

    elif opcao == "6":
        tarefas.clear()
        print("Todas estao removidas!")

    elif opcao == "7":
        tarefa = input("Que tarefa queres contar? ")
        print("Aparece", tarefas.count(tarefa), "vez(es).")

    elif opcao == "8":
        tarefa = input("Que tarefa queres procurar? ")
        if tarefa in tarefas:
            print("Primeira posição:", tarefas.index(tarefa))
        else:
            print("Essa tarefa não existe.")

    elif opcao == "9":
        tarefas.sort()
        print("Tarefas estão ordenadas!")

    elif opcao == "10":
        tarefas.reverse()
        print("Ordem esta invertida!")

    elif opcao == "11":
        copiat = tarefas.copy()
        print("Cópia feita:", copiat)

    elif opcao == "12":
        print("Tarefas:", tarefas)

    elif opcao == "0":
        print("Ate logo!")
        break

    else:
        print("Não existe essa opção")