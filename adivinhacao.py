import random


def jogar():
    print("************************************")
    print("Bem vindo ao jogo de adivinhção!")
    print("************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    menor_numero = 1
    maior_numero = 100
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1)Fácil (2)Médio (3)Dificil ")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero entre {} e {}: ".format(menor_numero, maior_numero))
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre {} e {}!".format(1, 100))
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Seu chute foi maior do que o número secreto.")
                maior_numero = chute
            elif menor:
                print("Seu chute foi menor do que o número secreto.")
                menor_numero = chute

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if rodada == total_de_tentativas:
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo.")


if __name__ == "__main__":
    jogar()
