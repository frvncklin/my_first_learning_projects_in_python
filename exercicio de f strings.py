nome = input("Insira seu nome: ")
idade = input("Digite sua idade: ")
quant_letras = len(nome) - nome.count(" ")
cabecalho = "ficha de cadastro".upper()

if nome == "" or idade == "":
    print("Desculpe, você deixou campos vazios.")
else:
    print("")
    print(f"{cabecalho:-^40}")
    print(f"NOME: {nome.upper()}\nIDADE: {idade}\n")
    print("SOBRE VOCÊ:")
    print(f"- Seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("- Seu nome contêm espaços.")
    elif " " not in nome:
        print("- Seu nome não contêm espaços.")

    print(f"- Seu nome contêm {quant_letras} letras.")
    print(f"- A primeira letra do seu nome é {nome[0]}.")
    print(f"- A última letra do seu nome é {nome[-1]}.")
    print(f"- Você nasceu no ano de {2023 - int(idade)}.")
