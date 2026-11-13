from random import randint, sample


def listar_inimigos_vivos(inimigos):
    vivos = [inimigo for inimigo in inimigos if inimigo["vida"] > 0]

    if len(vivos) == 0:
        print("Nao existem inimigos vivos.")
    else:
        print("\nInimigos vivos:")
        for numero, inimigo in enumerate(vivos, start=1):
            print(f"{numero} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")

    return vivos


def consultar_estado(jogador, inimigos):
    vivos = [inimigo for inimigo in inimigos if inimigo["vida"] > 0]
    derrotados = len(inimigos) - len(vivos)

    print("\nEstado do jogador:")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuacao: {jogador['pontos']}")
    print(f"Inimigos derrotados: {derrotados}")
    print(f"Inimigos vivos: {len(vivos)}")
    print(f"Pocoes disponiveis: {jogador['pocoes']}")
    print(f"Pontos recuperados: {jogador['pontos_recuperados']}")


def atacar_inimigo(jogador, inimigos):
    vivos = listar_inimigos_vivos(inimigos)

    while True:
        escolha = input("Escolhe o numero do inimigo: ").strip()
        try:
            numero = int(escolha)
        except ValueError:
            numero = 0

        if 1 <= numero <= len(vivos):
            inimigo = vivos[numero - 1]
            break
        print("Escolha invalida. Introduz um numero da lista.")

    dano = randint(10, jogador["ataque"])
    inimigo["vida"] = max(0, inimigo["vida"] - dano)
    print(f"Atacaste o {inimigo['nome']} e causaste {dano} pontos de dano.")

    if inimigo["vida"] == 0:
        jogador["pontos"] += inimigo["pontos"]
        print(f"Derrotaste o {inimigo['nome']} e ganhaste {inimigo['pontos']} pontos.")
    else:
        dano_inimigo = randint(5, inimigo["ataque"])
        jogador["vida"] = max(0, jogador["vida"] - dano_inimigo)
        print(f"O {inimigo['nome']} contra-atacou e causou {dano_inimigo} pontos de dano.")


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Ja nao tens pocoes.")
    elif jogador["vida"] >= 100:
        print("Nao podes usar uma pocao com 100 ou mais pontos de vida.")
    else:
        vida_antes = jogador["vida"]
        jogador["vida"] = min(100, jogador["vida"] + 25)
        pontos_recuperados = jogador["vida"] - vida_antes
        jogador["pontos_recuperados"] += pontos_recuperados
        jogador["pocoes"] -= 1
        print(f"Recuperaste {pontos_recuperados} pontos de vida.")


print("========== BATALHA ==========\n")

jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0,
    "pontos_recuperados": 0,
}

tipos_inimigo = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragao", "vida": 100, "ataque": 20, "pontos": 500},
]

numero_inimigos = randint(3, 5)
inimigos = sample(tipos_inimigo, numero_inimigos)
resultado = ""

while jogador["vida"] > 0 and len([inimigo for inimigo in inimigos if inimigo["vida"] > 0]) > 0:
    print("\n========== BATALHA ==========")
    print("1 - Atacar inimigo")
    print("2 - Consultar estado do jogador")
    print("3 - Listar inimigos vivos")
    print("4 - Usar pocao de cura")
    print("5 - Fugir / terminar jogo")

    opcao = input("Escolhe uma opcao: ").strip()

    if opcao == "1":
        atacar_inimigo(jogador, inimigos)
    elif opcao == "2":
        consultar_estado(jogador, inimigos)
    elif opcao == "3":
        listar_inimigos_vivos(inimigos)
    elif opcao == "4":
        usar_pocao(jogador)
    elif opcao == "5":
        resultado = "FUGA"
        break
    else:
        print("Opcao invalida. Tenta novamente.")

if resultado == "FUGA":
    print("\nPartida terminada por fuga.")
elif jogador["vida"] == 0:
    print("\nDerrota! O jogador ficou sem vida.")
else:
    print("\nVitoria! Todos os inimigos foram derrotados.")

consultar_estado(jogador, inimigos)