def contar_inimigos_vivos(inimigos):
    quantidade = 0

    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            quantidade = quantidade + 1

    return quantidade


def listar_inimigos_vivos(inimigos):
    print("\nInimigos vivos:")

    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            print(f"{inimigo['numero']} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")

    if contar_inimigos_vivos(inimigos) == 0:
        print("Nao existem inimigos vivos.")


def consultar_estado(jogador, inimigos):
    vivos = contar_inimigos_vivos(inimigos)
    total_inimigos = 0

    for inimigo in inimigos:
        total_inimigos = total_inimigos + 1

    derrotados = total_inimigos - vivos

    print("\nEstado do jogador:")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuacao: {jogador['pontos']}")
    print(f"Inimigos derrotados: {derrotados}")
    print(f"Inimigos vivos: {vivos}")
    print(f"Pocoes disponiveis: {jogador['pocoes']}")


def atacar_inimigo(jogador, inimigos):
    listar_inimigos_vivos(inimigos)
    encontrado = False
    inimigo_escolhido = {}

    while encontrado == False:
        escolha = input("Escolhe o numero do inimigo: ")

        for inimigo in inimigos:
            if inimigo["numero"] == escolha:
                if inimigo["vida"] > 0:
                    inimigo_escolhido = inimigo
                    encontrado = True

        if encontrado == False:
            print("Escolha invalida. Introduz o numero de um inimigo vivo.")

    dano = 10
    inimigo_escolhido["vida"] = inimigo_escolhido["vida"] - dano

    if inimigo_escolhido["vida"] < 0:
        inimigo_escolhido["vida"] = 0

    print(f"Atacaste o {inimigo_escolhido['nome']} e causaste {dano} pontos de dano.")

    if inimigo_escolhido["vida"] == 0:
        jogador["pontos"] = jogador["pontos"] + inimigo_escolhido["pontos"]
        print(f"Derrotaste o {inimigo_escolhido['nome']}.")
    else:
        dano_inimigo = 5
        jogador["vida"] = jogador["vida"] - dano_inimigo

        if jogador["vida"] < 0:
            jogador["vida"] = 0

        print(f"{inimigo_escolhido['nome']} contra-atacou e causou {dano_inimigo} pontos de dano.")


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Ja nao tens pocoes.")
    else:
        if jogador["vida"] >= 100:
            print("Nao podes usar uma pocao com 100 ou mais pontos de vida.")
        else:
            vida_antes = jogador["vida"]
            jogador["vida"] = jogador["vida"] + 25

            if jogador["vida"] > 100:
                jogador["vida"] = 100

            pontos_recuperados = jogador["vida"] - vida_antes
            jogador["pontos_recuperados"] = jogador["pontos_recuperados"] + pontos_recuperados
            jogador["pocoes"] = jogador["pocoes"] - 1
            print(f"Recuperaste {pontos_recuperados} pontos de vida.")


def menu():
    print("\n========== BATALHA ==========")
    print("1 - Atacar inimigo")
    print("2 - Consultar estado do jogador")
    print("3 - Listar inimigos vivos")
    print("4 - Usar pocao de cura")
    print("5 - Fugir / terminar jogo")
    return input("Escolhe uma opcao: ")
