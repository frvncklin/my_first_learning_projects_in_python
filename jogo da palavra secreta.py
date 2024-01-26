palavra_secreta = "coragem"
palavra_formatada = "*******"
tentativas = 0

print("------------Jogo da Palavra Secreta------------\n")
print('Tente adivinhar qual a palavra secreta!\nCada tentativa mostrará para você uma parte dessa palavra!\n\nVamos começar!')
print("Digite uma tentativa:")

while True: 

    entrada_user = input(">>> ")
    tentativas += 1

    if entrada_user != palavra_secreta:

        for letra_user in entrada_user:
            if letra_user in palavra_secreta:
                palavra_formatada = palavra_formatada.replace(palavra_formatada[palavra_secreta.index(letra_user)], letra_user, 1)
        print(f"Palavra Secreta: {palavra_formatada}")
        if palavra_formatada == palavra_secreta:
            break

    else:
        break

print(f"Parabéns, você ganhou! Você fez um total de {tentativas} tentativas.")
