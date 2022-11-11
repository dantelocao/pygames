import random

def abertura_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def retorna_sorteio():
    lista_palavras = []
    arquivo = open("palavras.txt", "r")
    for palavra in arquivo:
        palavra = palavra.strip()
        lista_palavras.append(palavra)
    sorteio = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[sorteio].upper()
    arquivo.close()
    return palavra_secreta
def pede_chute():
    chute = str(input("digite a letra: ")).strip().upper()
    return chute
def compara_letra(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1
def imprime_vencedor(acertou):
    if acertou:
        print("você venceu!!")
    else:
        print("voce perdeu")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    abertura_jogo()
    palavra_secreta = retorna_sorteio()
    print(palavra_secreta)  #depuração

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas = 7
    erros = 0
    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            compara_letra(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas = tentativas - 1
            erros = erros + 1
            desenha_forca(erros)
            print("\nnão foi achado nenhuma letra, mais {} tentativas".format(tentativas))

        print(letras_acertadas)
        letras_faltando = letras_acertadas.count('_')
        print("faltam {} letras para achar todas\n".format(letras_faltando))

        if letras_faltando == 0:
            acertou = True
        if tentativas == 0:
            enforcou = True

    imprime_vencedor(acertou)

if __name__ == "__main__":
    jogar()
