# ---------- Definindo a função para transformar as entradas do usuário em números ---------


def transformador_numero(numero_tranf):

    if numero_tranf.isdigit() == True:
        numero_tranf = int(numero_tranf)
        return numero_tranf

    elif numero_tranf.isdigit() == False:

        if "," in numero_tranf:
            numero_tranf = numero_tranf.replace(",", ".")
            numero_tranf = float(numero_tranf)
            return numero_tranf
        
        elif "." in numero_tranf:
            numero_tranf = float(numero_tranf)
            return numero_tranf

        else:
            return numero_tranf
        

# Executando o somador.

# Capturando a entrada do usuário.
numeros = input("Digite os números que Você deseja somar, um após o outro:\n(Separados por vírgulas. -> Ex: 1, 2, 3 = 1 + 2 + 3)\n(Caso seja decimal, utilize ponto \".\" -> Ex: 92.09)\n>>> ")

# Separando os items da entrada.
numeros = numeros.split(",")

# Transformando os items em números int ou float e tratando erros.
for indice, item in enumerate(numeros):
    numeros[indice] = numeros[indice].strip()
    numeros[indice] = transformador_numero(numeros[indice])

    # Se o programa detectar que o transformador falhou. Tratar o erro e corrigir o número.
    if type(numeros[indice]) == str:
        print(f"\n---> Você digitou o número inválido {numeros[indice]} ---> Por favor corrija-o:", end="")

        while True:
            numeros[indice] = input("\n>>> ")

            if type(transformador_numero(numeros[indice])) != str:
                numeros[indice] = transformador_numero(numeros[indice])
                break

print(f"\nA soma total destes números é:\n--------> {sum(numeros):.2f}")