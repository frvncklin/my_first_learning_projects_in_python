numero = input("Digite um número inteiro: ")

inteiro = numero.isdigit() == True
nao_inteiro = numero.isdigit() == False

if inteiro:
    numero = int(numero)
    numero_par = numero % 2 == 0
    numero_impar = numero % 2 != 0

    if numero_par:
        print('Este número é par.')
    elif numero_impar:
        print("Este número é ímpar")

else:
    print("Você não digitou um número inteiro")