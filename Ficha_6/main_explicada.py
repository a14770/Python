from random import randint


# Conta inimigos vivos percorrendo a lista.
def contar_inimigos_vivos(inimigos):
    quantidade = 0

    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            quantidade = quantidade + 1

    return quantidade


def listar_inimigos_vivos(inimigos):
    quantidade = 0

    print("\nInimigos vivos:")
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            print(f"{inimigo['numero']} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")
            quantidade = quantidade + 1

    if quantidade == 0:
        print("Nao existem inimigos vivos.")


def consultar_estado(jogador, inimigos):
    vivos = contar_inimigos_vivos(inimigos)
    derrotados = len(inimigos) - vivos

    print("\nEstado do jogador:")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuacao: {jogador['pontos']}")
    print(f"Inimigos derrotados: {derrotados}")
    print(f"Inimigos vivos: {vivos}")
    print(f"Pocoes disponiveis: {jogador['pocoes']}")
    print(f"Pontos recuperados: {jogador['pontos_recuperados']}")


def atacar_inimigo(jogador, inimigos):
    listar_inimigos_vivos(inimigos)
    encontrado = False
    inimigo_escolhido = {}

    # Compara a resposta com os numeros apresentados no ecra.
    while encontrado == False:
        escolha = input("Escolhe o numero do inimigo: ")

        for inimigo in inimigos:
            if inimigo["numero"] == escolha:
                if inimigo["vida"] > 0:
                    inimigo_escolhido = inimigo
                    encontrado = True

        if encontrado == False:
            print("Escolha invalida. Introduz o numero de um inimigo vivo.")

    dano = randint(10, jogador["ataque"])
    inimigo_escolhido["vida"] = inimigo_escolhido["vida"] - dano

    # Corrige a vida se o dano for maior do que a vida restante.
    if inimigo_escolhido["vida"] < 0:
        inimigo_escolhido["vida"] = 0

    print(f"Atacaste o {inimigo_escolhido['nome']} e causaste {dano} pontos de dano.")

    if inimigo_escolhido["vida"] == 0:
        jogador["pontos"] = jogador["pontos"] + inimigo_escolhido["pontos"]
        print(f"Derrotaste o {inimigo_escolhido['nome']} e ganhaste {inimigo_escolhido['pontos']} pontos.")
    else:
        dano_inimigo = randint(5, inimigo_escolhido["ataque"])
        jogador["vida"] = jogador["vida"] - dano_inimigo

        if jogador["vida"] < 0:
            jogador["vida"] = 0

        print(f"O {inimigo_escolhido['nome']} contra-atacou e causou {dano_inimigo} pontos de dano.")


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Ja nao tens pocoes.")
    else:
        if jogador["vida"] >= 100:
            print("Nao podes usar uma pocao com 100 ou mais pontos de vida.")
        else:
            vida_antes = jogador["vida"]
            jogador["vida"] = jogador["vida"] + 25

            # Limita a vida a 100 quando a cura ultrapassa esse valor.
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


print("========== BATALHA ==========\n")

jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0,
    "pontos_recuperados": 0,
}

tipos_inimigo = [
    {"numero": "1", "nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"numero": "2", "nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"numero": "3", "nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"numero": "4", "nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"numero": "5", "nome": "Dragao", "vida": 100, "ataque": 20, "pontos": 500},
]

# Escolhe 3 a 5 inimigos sem repetir, retirando cada escolhido da lista.
numero_inimigos = randint(3, 5)
inimigos = []

for _ in range(numero_inimigos):
    indice = randint(0, len(tipos_inimigo) - 1)
    inimigo = tipos_inimigo.pop(indice)
    inimigos.append(inimigo)

resultado = ""

while True:
    # Termina a batalha quando o jogador perde ou nao ha inimigos vivos.
    if jogador["vida"] <= 0:
        break

    if contar_inimigos_vivos(inimigos) == 0:
        break

    opcao = menu()

    if opcao == "1":
        atacar_inimigo(jogador, inimigos)
    if opcao == "2":
        consultar_estado(jogador, inimigos)
    if opcao == "3":
        listar_inimigos_vivos(inimigos)
    if opcao == "4":
        usar_pocao(jogador)
    if opcao == "5":
        resultado = "FUGA"
        break
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Opcao invalida. Tenta novamente.")

if resultado == "FUGA":
    print("\nPartida terminada por fuga.")
else:
    if jogador["vida"] == 0:
        print("\nDerrota! O jogador ficou sem vida.")
    else:
        print("\nVitoria! Todos os inimigos foram derrotados.")

consultar_estado(jogador, inimigos)
