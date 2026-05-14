# Exercício 7.10
# Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
# posição está livre. Verifique também quando um jogador venceu a partida. Um jogo da velha pode ser visto como uma lista de três elementos, na qual cada
# elemento é outra lista, também com três elementos.

print("======== Exercício 7.10 ========\n")

print("""

Utilize o mapa abaixo para realizar suas jogadas:

 7 | 8 | 9 
---+---+---
 4 | 5 | 6 
---+---+---
 1 | 2 | 3
""")

tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

coordenadas_tabuleiro = {
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (0, 0),
    8: (0, 1),
    9: (0, 2)
}

jogador = "Jogador 1"
jogadas = 0
venceu = False

while not venceu and jogadas < 9:
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
    print("---+---+---")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
    print("---+---+---")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")

    jogada = input(f"\n{jogador} - Digite o número da posição a ser marcada: ")
    print()

    if jogada.isdigit():
        jogada = int(jogada)
    else:
        print("Entrada inválida! Digite apenas números de 1 a 9.\n")
        continue

    if jogada in coordenadas_tabuleiro:
        linha, coluna = coordenadas_tabuleiro[jogada]
    else:
        print("Jogada inválida! Digite um número entre 1 e 9.\n")
        continue

    if tabuleiro[linha][coluna] == ' ':
        if jogador == "Jogador 1":
            tabuleiro[linha][coluna] = 'X'
            jogadas += 1
        else:
            tabuleiro[linha][coluna] = 'O'
            jogadas += 1
    else:
        print("Posição ocupada. Escolha outra posição.\n")
        continue

    for casa_1, casa_2, casa_3 in tabuleiro:
        if casa_1 != " " and casa_1 == casa_2 and casa_2 == casa_3:
            venceu = True

    for coluna in range(3):
        if tabuleiro[0][coluna] != " " and tabuleiro[0][coluna] == tabuleiro[1][coluna] and tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            venceu = True

    if tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        venceu = True

    if tabuleiro[2][0] != " " and tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][2]:
        venceu = True

    if venceu:
        print(f"{jogador} venceu a partida!\n")
        print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")
    elif jogadas == 9:
        print("Partida empatada!\n")
        print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("---+---+---")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")
    else:
        if jogador == "Jogador 1":
            jogador = "Jogador 2"
        else:
            jogador = "Jogador 1"
