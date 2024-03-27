import os

while True:

    print("------------ GERADOR DE CPF ------------\n\nautor: daemon.dev\n\n")
    cpf = input("Digite os 9 primeiros dígitos do seu CPF (somente números):\n>>> ")

    if len(cpf) != 9 and cpf.isdigit() == True:

        os.system("cls")       
        print("Você precisa digitar todos os 9 dígitos do CPF!\nVamos tentar novamente.\n\n.................\n")
        continue

    elif cpf.isdigit() == False:

        os.system("cls")       
        print("Há uma letra no CPF, digite somente números!\nVamos tentar novamente.\n\n.................\n")
        continue

    else:



        # ---------- Calculando primeiro dígito. ----------



        # Criando variáveis e listas para cálculo do primeiro e do segundo dígito
        # OBS: Estas variáveis e listas serão usadas para o cálculo de ambos, embora de maneiras diferentes.

        lista_numeros_cpf = []
        lista_numeros_cpf_calculo = []  
        validador = 10          
        gerador_de_digito = 0     

        for numero in cpf:
            lista_numeros_cpf.append(numero)

        # Executando o cálculo do primeiro dígito.
        
        for indice, digito in enumerate(lista_numeros_cpf):
            digito = int(digito) * validador
            lista_numeros_cpf_calculo.append(digito)
            gerador_de_digito += lista_numeros_cpf_calculo[indice]
            validador -= 1
            
        gerador_de_digito = (gerador_de_digito * 10) % 11

        primeiro_digito = 0 if gerador_de_digito > 9 else gerador_de_digito



        # ---------- Calculando segundo dígito. ----------



        # Adicionando o primeiro dígito ao à lista de números do CPF:

        lista_numeros_cpf.append(primeiro_digito)

        # Zerando as variáveis e listas para calcular o segundo dígito.

        lista_numeros_cpf_calculo = []
        validador = 11      # Neste caso, o validador deve ser 11.
        gerador_de_digito = 0

        # Executando o cálculo do segundo dígito.

        for indice, digito in enumerate(lista_numeros_cpf):
            digito = int(digito) * validador
            lista_numeros_cpf_calculo.append(digito)
            gerador_de_digito += lista_numeros_cpf_calculo[indice]
            validador -= 1

        gerador_de_digito = (gerador_de_digito * 10) % 11

        segundo_digito = 0 if gerador_de_digito > 9 else gerador_de_digito


        # Adicionando o segundo dígito ao à lista de números do CPF:

        lista_numeros_cpf.append(segundo_digito)



        # ---------- Modelando o CPF. ----------


        cpf_corrigido = ''

        for indice, digito in enumerate(lista_numeros_cpf):

            if (indice + 1) < 9:
                cpf_corrigido += str(digito)

                if (indice + 1) % 3 == 0:
                    cpf_corrigido += "."

            else:

                if (indice + 1) == 9:
                    cpf_corrigido += "-"

                elif (indice + 1) == 10:
                    cpf_corrigido += str(f"{primeiro_digito}")
            
                elif (indice + 1) == 11:
                    cpf_corrigido += str(f"{segundo_digito}")

        print(f"\n---> O seu CPF será: {cpf_corrigido}") 



        # ------------> CPF GERADO COM SUCESSO. <-------------

    
    # Dando a opção ao usuário para reiniciar o programa e gerar outro cpf:


    escolha = input("\n.........................\nDeseja continuar? 1 - sim ou 2 - não.\n>>> ")

    if escolha.startswith('1'):
        os.system("cls")
    else:
        os.system("cls")
        print("Encerrando! Muito obrigado!")
        break
