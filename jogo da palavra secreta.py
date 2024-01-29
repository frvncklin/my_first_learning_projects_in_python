palavra_secreta = "coragem"
letras_acertadas = ""
tentativas = 0

print("------------Jogo da Palavra Secreta------------\n")
print('Tente adivinhar qual a palavra secreta!\nCada tentativa mostrará para você uma parte dessa palavra!\n\nVamos começar!')
print("Digite uma tentativa:")

while True: 

    entrada_user = input(">>> ").lower()

    if entrada_user != palavra_secreta:

        for letra_user in entrada_user:         # Para cada uma das letras do usuário.

            if letra_user in palavra_secreta and letra_user not in letras_acertadas:       # Verificar se elas estão na palavra secreta.
                letras_acertadas += letra_user

        palavra_formatada = ""

        for letra_secreta in palavra_secreta:

            if letra_secreta in letras_acertadas:
                palavra_formatada += letra_secreta
            else: 
                palavra_formatada += "*"

        if palavra_formatada == palavra_secreta:
            break

        tentativas += 1
        print(f"Palavra secreta: {palavra_formatada}")
    
    else:
        break

print(f"Parabéns, você ganhou! A apalvra secreta era {palavra_secreta}!\nVocê fez um total de {tentativas} tentativas.")
