from ficha7_ex1 import atacar_inimigo, consultar_estado, contar_inimigos_vivos, listar_inimigos_vivos, menu, usar_pocao


print("========== BATALHA ==========")

jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0,
    "pontos_recuperados": 0,
}

inimigos = [
    {"numero": "1", "nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"numero": "2", "nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"numero": "3", "nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
]

resultado = ""
opcao = menu()

while True:
    if jogador["vida"] <= 0:
        break

    if contar_inimigos_vivos(inimigos) == 0:
        break

    if opcao == "1":
        atacar_inimigo(jogador, inimigos)
    else:
        if opcao == "2":
            consultar_estado(jogador, inimigos)
        else:
            if opcao == "3":
                listar_inimigos_vivos(inimigos)
            else:
                if opcao == "4":
                    usar_pocao(jogador)
                else:
                    if opcao == "5":
                        resultado = "FUGA"
                        break
                    else:
                        print("Opcao invalida. Tenta novamente.")

    if jogador["vida"] > 0:
        if contar_inimigos_vivos(inimigos) > 0:
            opcao = menu()

if resultado == "FUGA":
    print("\nPartida terminada por fuga.")
else:
    if jogador["vida"] == 0:
        print("\nDerrota! O jogador ficou sem vida.")
    else:
        print("\nVitoria! Todos os inimigos foram derrotados.")

consultar_estado(jogador, inimigos)
