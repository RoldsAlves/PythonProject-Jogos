import random


def jogar():
    imprime_mensgem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acetadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não acertar ou não se enforcar
    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            letras_acertadas = marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            dica(erros)
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_vencedor()
    else:
        imprime_enforcado(palavra_secreta)
    print("Fim do jogo.")


def dica(erros):
    if erros == 3:
        print("Dica: A palavra é o nome de uma fruta.")


def desenha_forca(erros):
    print("voce errou {} de 6".format(erros))
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_vencedor():
    print("Parabéns, você ganhou!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:       /-.    ")
    print("     | (|:.      |) |   ")
    print("      '-|:.      |-'    ")
    print("        \::     /       ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_enforcado(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def imprime_mensgem_abertura():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")


def inicializa_letras_acetadas(palavra_secreta):
    return ["_" for _ in palavra_secreta]


def pede_chute():
    chute = input("Qual a letra?: ")
    return chute.strip().upper()


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1
    return letras_acertadas


if __name__ == "__main__":
    jogar()
