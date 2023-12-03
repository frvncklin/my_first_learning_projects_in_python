numero = input("Digite um número inteiro: ")

inteiro = numero.isdigit() == True

if inteiro:
    numero = int(numero)
    numero_par = numero % 2 == 0
    numero_impar = numero % 2 != 0

    if numero_par:
        print(f'O número {numero} é par.')
    elif numero_impar:
        print(f'O número {numero} é ímpar.')

else:
    print("Você não digitou um número inteiro!")
