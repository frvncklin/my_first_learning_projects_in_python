import os

while True:

    cpf = input("Digite os 9 primeiros dígitos do seu CPF (somente números):\n>>> ")

    if len(cpf) != 9:

        os.system("cls")       
        print("Você precisa digitar todos os 9 dígitos do CPF!\nVamos tentar novamente.\n\n.................\n\n")
        continue

    elif cpf.isdigit() == False:

        os.system("cls")       
        print("Há uma letra no CPF, digite somente números!\nVamos tentar novamente.\n\n.................\n\n")
        continue

    else:

        lista_numeros_cpf = []
        lista_numeros_cpf_calculo = []
        validador = 10          
        determinante_primeiro_digito = 0 
        cpf_corrigido = ''

        for numero in cpf:
            lista_numeros_cpf.append(numero)
        
        for indice, digito in enumerate(lista_numeros_cpf):
            digito = int(digito) * validador
            lista_numeros_cpf_calculo.append(digito)
            determinante_primeiro_digito += lista_numeros_cpf_calculo[indice]
            validador -= 1

        # Realizando operações no determinate do primeiro dígito.
            
        determinante_primeiro_digito = (determinante_primeiro_digito * 10) % 11

        primeiro_digito = 0 if determinante_primeiro_digito > 9 else determinante_primeiro_digito

        # Modelando o CPF:

        for indice, digito in enumerate(lista_numeros_cpf):

            cpf_corrigido += str(digito)

            if (indice + 1) % 3 == 0 and (indice + 1) < 9:
                cpf_corrigido += "."
            
            elif indice == 8:
                cpf_corrigido += "-"
                cpf_corrigido += str(f"{primeiro_digito}")
                cpf_corrigido += "X"

        print(f"\n---> O seu CPF será: {cpf_corrigido}")    

    escolha = input("\n.........................\nDeseja continuar? 1 - sim ou 2 - não.\n>>> ")

    if escolha.startswith('1'):
        os.system("cls")
    else:
        os.system("cls")
        print("Encerrando! Muito obrigado!")
        break
