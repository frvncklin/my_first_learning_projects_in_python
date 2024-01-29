palavra_secreta = "coragem"
letras_acertadas = ""
tentativas = 0

print("------------Jogo da Palavra Secreta------------\n")
print('Tente adivinhar qual a palavra secreta!\nCada tentativa mostrará para você uma parte dessa palavra!\n\nVamos começar!')
print("Digite uma tentativa:")

while True: 

    entrada_user = input(">>> ").lower()

    for letra_user in entrada_user:         # Para cada uma das letras do usuário.

        if letra_user in palavra_secreta and letra_user not in letras_acertadas:       # Verificar se elas estão na palavra secreta.
            letras_acertadas += letra_user

    palavra_formatada = ""
    tentativas += 1

    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else: 
            palavra_formatada += "*"

    if palavra_formatada == palavra_secreta:
        print(f"\n---> Palavra secreta: {palavra_formatada}.\n\nParabéns, você ganhou!\nVocê fez um total de {tentativas} tentativas.")
        escolha = input("\nDeseja jogar de novo? Digite 1 - sim ou 2 - não.\n>>> ")
        if escolha == '1':
            print("................Retornando................\n\n")
            print("Digite uma tentativa:")
            letras_acertadas = ""
            tentativas = 0
        else:
            print("\nMuito obrigado e até logo!\nautor: Victor Francklin\n\n.................................")
            break

    else:
        print(f"Palavra secreta: {palavra_formatada}.")
        continue
