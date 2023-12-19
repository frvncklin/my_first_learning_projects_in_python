""" Calculadora com while"""
mensagem = "Bem vindos à CALCULADORA INTELIGENTE"
cabecalho = f"{mensagem:-^50}\n"
print(cabecalho)
print("Agora, você vai digitar o primeiro número, depois o operador e então digitar o segundo número.\n")

contador = True

while contador == True:

    # Recebendo os inputs do usuário => Primeiro número, operação e segundo número.

    numero_um = input("Digite um primeiro número:\n>>> ")
    operador = input("Digite a letra do operador:\n[ a - adição, s - subitração, m - multiplicação, d - divisão, p - potenciação ]\n>>> ")
    numero_dois = input("Digite o segundo número:\n>>> ")

    # Definindo opções de conversão dos inputs dos números.

    inteiro_numero_um = numero_um.isdigit() == True
    nao_inteiro_numero_um = numero_um.isdigit() == False
    inteiro_numero_dois = numero_dois.isdigit() == True
    nao_inteiro_numero_dois = numero_dois.isdigit() == False
    
    # numero_um

    if inteiro_numero_um:     # Caso seja inteiro.
        numero_um = int(numero_um)
    elif nao_inteiro_numero_um:  # Caso não seja inteiro.
        if "." in numero_um:
            numero_um = float(numero_um)
        elif "," in numero_um:
            numero_um = numero_um.replace(",", ".")
            numero_um = float(numero_um)
        else:
            print("Você não digitou um número!!")
            contador = False
    
    # numero_dois

    if inteiro_numero_dois:     # Caso seja inteiro.
        numero_dois = int(numero_dois)
    elif nao_inteiro_numero_dois:  # Caso não seja inteiro.
        if "." in numero_dois:
            numero_dois = float(numero_dois)
        elif "," in numero_dois:
            numero_dois = numero_dois.replace(",", ".")
            numero_dois = float(numero_dois)
        else:
            print("Você não digitou um número!!")
            contador = False

    # Definindo operações.

    adicao = operador == "a"
    subtracao = operador == "s"
    multiplicacao = operador == "m"
    divisao = operador == "d"
    potenciacao = operador == "p"


    # Definindo branches dos resultados.

    if adicao:
        resultado = numero_um + numero_dois
        print(f"\nO resultado é: {resultado}")
    elif subtracao:
        resultado = (numero_um) - (numero_dois)
        print(f"\nO resultado é: {resultado}")
    elif multiplicacao:
        resultado = (numero_um) * (numero_dois)
        print(f"\nO resultado é: {resultado}")
    elif divisao:
        resultado = (numero_um) / (numero_dois)
        print(f"\nO resultado é: {resultado:.2f}")
    elif potenciacao:
        resultado = (numero_um) ** (numero_dois)
        print(f"\nO resultado é: {resultado}")
    else:
        print("Você não digitou um operador válido!")
    
    # Definindo escolha de continuidade do loop.

    continuidade = input("Você deseja continuar? Digite 1 para sim ou 2 para não: ")
    if continuidade == "1":
        print("Ok! Vamos seguir!\n................\n")
    elif continuidade == "2":
        print("Então encerramos! Muito obrigado!")
        contador = False

mensagem_final = "PROGRAMA ENCERRADO"
print(f"\n{mensagem_final:-^50}")