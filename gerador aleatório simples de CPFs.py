import random
import os

while True:

    print("------------ GERADOR ALEATÓRIO DE CPFs ------------\n\nautor: daemon.dev\n")

    quantidade = input("\nDigite quantos CPFs você deseja gerar:\n>>> ")

    if quantidade.isdigit() == True:
        quantidade = int(quantidade) 
        break
    else:
        os.system("cls")
        print("Você precisa digitar um número inteiro! Tente novamente.\n\n.................\n")



print("-----------------------\n")
for i in range(quantidade):

    cpf = ''
    gerador_de_digito = 0
    contador = 0
    validador = 10

    # Gerando o CPF aleatório (ao mesmo tempo, começando a calcular o primeiro dígito).

    for contador in range(9):

        numero = random.randint(0, 9)
        cpf += str(numero)
        numero = numero * validador
        gerador_de_digito += numero
        validador -= 1

    # Gerando o primeiro dígito e adicionando ele ao CPF.

    gerador_de_digito = (gerador_de_digito * 10) % 11

    primeiro_digito = 0 if gerador_de_digito > 9 else gerador_de_digito

    cpf += str(primeiro_digito)

    # Calculando o segundo dígito.

    validador = 11
    gerador_de_digito = 0

    for contador in range(10):
        numero = int(cpf[contador])
        numero = numero * validador
        gerador_de_digito += numero
        validador -= 1

    # Gerando o segundo dígito e adicionando ele ao CPF.

    gerador_de_digito = (gerador_de_digito * 10) % 11

    segundo_digito = 0 if gerador_de_digito > 9 else gerador_de_digito

    cpf += str(segundo_digito)

    # Modelando o CPF:

    cpf_corrigido = ''
    contador = 0

    for digito in cpf:
        
        cpf_corrigido += digito
     
        if (contador + 1) < 9:
         
            if (contador + 1) % 3 == 0:
             
                cpf_corrigido += "."
    
        elif (contador + 1) >= 9:

            if (contador + 1) == 9:

                cpf_corrigido += "-"
        
        contador += 1
    
        
    print(cpf_corrigido)

             







