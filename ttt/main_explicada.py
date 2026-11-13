# Importa randint para sortear valores e sample para escolher inimigos sem repeticao.
from random import randint, sample


# Define uma funcao que recebe a lista de inimigos da batalha.
def listar_inimigos_vivos(inimigos):
    # Cria uma lista nova apenas com inimigos cuja vida ainda e maior que zero.
    vivos = [inimigo for inimigo in inimigos if inimigo["vida"] > 0]

    # Verifica se a lista de inimigos vivos ficou vazia.
    if len(vivos) == 0:
        # Informa que ja nao ha inimigos para mostrar.
        print("Nao existem inimigos vivos.")
    # Executa este bloco quando existe pelo menos um inimigo vivo.
    else:
        # Mostra um titulo antes da lista.
        print("\nInimigos vivos:")
        # Percorre os inimigos e cria numeros de escolha a partir de 1.
        for numero, inimigo in enumerate(vivos, start=1):
            # Mostra numero, nome, vida e ataque do inimigo.
            print(f"{numero} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")

    # Devolve a lista para outras funcoes poderem usar os inimigos vivos.
    return vivos


# Define uma funcao para mostrar os dados atuais do jogador e da batalha.
def consultar_estado(jogador, inimigos):
    # Guarda numa lista apenas os inimigos que ainda nao foram derrotados.
    vivos = [inimigo for inimigo in inimigos if inimigo["vida"] > 0]
    # Calcula os derrotados subtraindo os vivos ao total de inimigos.
    derrotados = len(inimigos) - len(vivos)

    # Imprime um titulo para separar esta informacao no ecra.
    print("\nEstado do jogador:")
    # Consulta no dicionario a vida atual do jogador.
    print(f"Vida: {jogador['vida']}")
    # Consulta no dicionario a pontuacao acumulada.
    print(f"Pontuacao: {jogador['pontos']}")
    # Mostra quantos inimigos foram derrotados.
    print(f"Inimigos derrotados: {derrotados}")
    # Mostra quantos inimigos continuam vivos.
    print(f"Inimigos vivos: {len(vivos)}")
    # Mostra quantas pocoes ainda estao disponiveis.
    print(f"Pocoes disponiveis: {jogador['pocoes']}")
    # Mostra o total de vida que o jogador recuperou durante o jogo.
    print(f"Pontos recuperados: {jogador['pontos_recuperados']}")


# Define a funcao que trata um ataque do jogador.
def atacar_inimigo(jogador, inimigos):
    # Mostra os inimigos vivos e guarda a lista devolvida pela funcao.
    vivos = listar_inimigos_vivos(inimigos)

    # Repete a pergunta ate o jogador introduzir um numero valido.
    while True:
        # Le a escolha como texto e retira espacos no inicio e no fim.
        escolha = input("Escolhe o numero do inimigo: ").strip()
        # Tenta converter a resposta para um numero inteiro.
        try:
            # Guarda a escolha numerica para validar e aceder a lista.
            numero = int(escolha)
        # Trata respostas que nao podem ser convertidas para inteiro.
        except ValueError:
            # Usa zero para que a verificacao seguinte considere a escolha invalida.
            numero = 0

        # Confirma que o numero esta entre 1 e a quantidade de inimigos vivos.
        if 1 <= numero <= len(vivos):
            # As listas comecam no indice zero, por isso subtrai um ao numero escolhido.
            inimigo = vivos[numero - 1]
            # Sai do ciclo porque a escolha ja e valida.
            break
        # Informa do erro e deixa o ciclo pedir outra escolha.
        print("Escolha invalida. Introduz um numero da lista.")

    # Sorteia o dano do jogador entre 10 e o seu ataque base.
    dano = randint(10, jogador["ataque"])
    # Retira o dano, mas usa max para impedir que a vida fique negativa.
    inimigo["vida"] = max(0, inimigo["vida"] - dano)
    # Mostra quanto dano foi causado.
    print(f"Atacaste o {inimigo['nome']} e causaste {dano} pontos de dano.")

    # Verifica se o ataque reduziu a vida do inimigo a zero.
    if inimigo["vida"] == 0:
        # Acrescenta a pontuacao deste inimigo aos pontos do jogador.
        jogador["pontos"] += inimigo["pontos"]
        # Informa que o inimigo foi derrotado e mostra os pontos ganhos.
        print(f"Derrotaste o {inimigo['nome']} e ganhaste {inimigo['pontos']} pontos.")
    # Se o inimigo ainda tiver vida, ele pode contra-atacar.
    else:
        # Sorteia o contra-ataque entre 5 e o valor de ataque do inimigo.
        dano_inimigo = randint(5, inimigo["ataque"])
        # Retira vida do jogador sem permitir um valor abaixo de zero.
        jogador["vida"] = max(0, jogador["vida"] - dano_inimigo)
        # Mostra quanto dano o jogador recebeu.
        print(f"O {inimigo['nome']} contra-atacou e causou {dano_inimigo} pontos de dano.")


# Define a funcao que verifica as regras e usa uma pocao de cura.
def usar_pocao(jogador):
    # Verifica primeiro se o jogador ainda tem pocoes.
    if jogador["pocoes"] == 0:
        # Avisa que nao e possivel curar sem pocoes.
        print("Ja nao tens pocoes.")
    # Impede usar uma pocao quando a vida ja e 100 ou mais.
    elif jogador["vida"] >= 100:
        # Avisa que a vida atual nao permite usar a pocao.
        print("Nao podes usar uma pocao com 100 ou mais pontos de vida.")
    # So chega aqui se houver pocoes e a vida for inferior a 100.
    else:
        # Guarda a vida antes de curar para calcular quanto foi recuperado.
        vida_antes = jogador["vida"]
        # Soma 25 de vida, mas limita o resultado a 100 pontos.
        jogador["vida"] = min(100, jogador["vida"] + 25)
        # Calcula a cura real, que pode ser inferior a 25 se atingir o limite.
        pontos_recuperados = jogador["vida"] - vida_antes
        # Atualiza o total acumulado de pontos recuperados.
        jogador["pontos_recuperados"] += pontos_recuperados
        # Retira uma pocao do inventario do jogador.
        jogador["pocoes"] -= 1
        # Informa quantos pontos de vida foram recuperados.
        print(f"Recuperaste {pontos_recuperados} pontos de vida.")


# Imprime o titulo do jogo antes de comecar a partida.
print("========== BATALHA ==========\n")

# Cria o dicionario do jogador com os valores pedidos no enunciado.
jogador = {
    # Define a vida inicial do jogador.
    "vida": 300,
    # Define o ataque base usado para sortear o dano.
    "ataque": 20,
    # Define que o jogador comeca com duas pocoes.
    "pocoes": 2,
    # Define a pontuacao inicial como zero.
    "pontos": 0,
    # Guarda o total de pontos de vida recuperados, inicialmente zero.
    "pontos_recuperados": 0,
}

# Cria uma lista com um dicionario para cada tipo de inimigo.
tipos_inimigo = [
    # Guarda o nome, a vida, o ataque e os pontos do Goblin.
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    # Guarda o nome, a vida, o ataque e os pontos do Orc.
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    # Guarda o nome, a vida, o ataque e os pontos do Troll.
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    # Guarda o nome, a vida, o ataque e os pontos do Beast.
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    # Guarda o nome, a vida, o ataque e os pontos do Dragao.
    {"nome": "Dragao", "vida": 100, "ataque": 20, "pontos": 500},
]

# Sorteia quantos inimigos vao participar: o minimo e 3 e o maximo e 5.
numero_inimigos = randint(3, 5)
# Escolhe essa quantidade de tipos diferentes de inimigos.
inimigos = sample(tipos_inimigo, numero_inimigos)
# Prepara uma variavel vazia para guardar se o jogador fugiu.
resultado = ""

# Repete o menu enquanto o jogador esta vivo e ainda ha inimigos vivos.
while jogador["vida"] > 0 and len([inimigo for inimigo in inimigos if inimigo["vida"] > 0]) > 0:
    # Mostra o titulo do menu em cada volta do ciclo.
    print("\n========== BATALHA ==========")
    # Mostra a opcao para atacar.
    print("1 - Atacar inimigo")
    # Mostra a opcao para consultar o estado.
    print("2 - Consultar estado do jogador")
    # Mostra a opcao para listar inimigos vivos.
    print("3 - Listar inimigos vivos")
    # Mostra a opcao para usar uma pocao.
    print("4 - Usar pocao de cura")
    # Mostra a opcao para fugir e terminar a partida.
    print("5 - Fugir / terminar jogo")

    # Le a opcao escolhida e remove espacos extra.
    opcao = input("Escolhe uma opcao: ").strip()

    # Se a opcao for 1, executa a funcao de ataque.
    if opcao == "1":
        # Passa o jogador e a lista de inimigos para a funcao.
        atacar_inimigo(jogador, inimigos)
    # Se a opcao for 2, mostra o estado atual.
    elif opcao == "2":
        # Passa os dados necessarios para calcular e mostrar o estado.
        consultar_estado(jogador, inimigos)
    # Se a opcao for 3, mostra os inimigos que ainda estao vivos.
    elif opcao == "3":
        # A funcao tambem informa se ja nao existem inimigos vivos.
        listar_inimigos_vivos(inimigos)
    # Se a opcao for 4, tenta usar uma pocao.
    elif opcao == "4":
        # A funcao verifica as regras antes de alterar os dados do jogador.
        usar_pocao(jogador)
    # Se a opcao for 5, regista a fuga e termina o ciclo.
    elif opcao == "5":
        # Guarda a fuga para mostrar a mensagem correta depois do ciclo.
        resultado = "FUGA"
        # Sai do ciclo principal imediatamente.
        break
    # Trata qualquer opcao que nao exista no menu.
    else:
        # Mostra o erro; o ciclo volta ao inicio e mostra novamente o menu.
        print("Opcao invalida. Tenta novamente.")

# Verifica se o ciclo terminou porque o jogador escolheu fugir.
if resultado == "FUGA":
    # Mostra a mensagem especifica de fuga.
    print("\nPartida terminada por fuga.")
# Se nao fugiu, verifica se o jogador ficou sem vida.
elif jogador["vida"] == 0:
    # Mostra a mensagem de derrota.
    print("\nDerrota! O jogador ficou sem vida.")
# Se nao fugiu nem perdeu, todos os inimigos foram derrotados.
else:
    # Mostra a mensagem de vitoria.
    print("\nVitoria! Todos os inimigos foram derrotados.")

# No fim, mostra a pontuacao e o estado final da partida.
consultar_estado(jogador, inimigos)