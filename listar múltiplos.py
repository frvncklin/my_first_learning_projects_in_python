# Vamos construir um programa para listar múltiplos de um número.

negativo = False
# Por razões de segurança, limitaremos a 8 algarismos no máximo.

import os

# --------------- Definindo funções que iremos utilizar ------------------:

def transformador_numero_inteiro(numero):     # Essa função vai verificar e transformar as entradas do usuário em um número inteiro, retornando com ele transformado.

    # Chamando a variável global "negativo" para detectar os números negativos.
    global negativo 

    # Caso o parãmetro seja inteiro e tiver até 8 algarismos, transformar a str de entrada em um int diretamente.
    if numero.isdigit() == True:

        negativo == False
        numero = int(numero)
        copia_numero_para_teste_de_len = str(numero)
        if len(copia_numero_para_teste_de_len) <= 8:
            return numero
        else:
            numero = str(numero)
        # Fiz esse processo para eliminar os zeros caso o usuário digite um zero na frente.

    # Se não for inteiro e/ou tiver mais de 9 algarismos, criar um loop que será quebrado assim que o usuário digitar um número inteiro válido.
    if numero.isdigit() == False or len(numero) > 8:       

        # Se ele for um inteiro negativo:
        if numero.startswith("-"):
            
            # Sinalizar que ele é negativo, utilizando a variável "negativo".
            negativo = True
            numero = numero.replace("-", "")

            # Convertê-lo e retornar o valor, com a variável "negativo" == True

            if numero.isdigit() == True:

                numero = int(numero)
                copia_numero_para_teste_de_len = str(numero)
                if len(copia_numero_para_teste_de_len) <= 8:
                    return numero
        
        # Se não for inteiro negativo, neste caso é inválido, então entramos no loop.

        print("\nOps! -> Você digitou um número inválido, tente novamente! Apenas inteiros:")

        while True: 

            negativo = False
            numero = input(">>> ")
            # Quando o número digitado for válido, convertê-lo e quebrar o loop.
            if numero.isdigit() == True:

                numero = int(numero)
                copia_numero_para_teste_de_len = str(numero)
                if len(copia_numero_para_teste_de_len) <= 8:
                    break

            elif numero.isdigit() == False:

                if numero.startswith("-"):

                    negativo == True
                    numero = numero.replace("-", "")

                    if numero.isdigit() == True:

                        numero = int(numero)
                        copia_numero_para_teste_de_len = str(numero)
                        if len(copia_numero_para_teste_de_len) <= 8:
                            return numero
                        
                else: 
                    continue

        # Assim que o número for válido e convertido, retornar com ele
        return numero
    
    
def encontrar_multiplo(numero):      # Essa função encontra todos os número múltiplos do parâmetro escolhido, a partir de 1.

    # Criando a lista para colocar os múltiplos do numero.
    multiplos = []

    # Percorrendo todos os possíveis múltiplos do numero.
    for possibilidade in range(1, numero + 1):         

        # Capturando os números que são múltiplos do número.
        if numero % possibilidade == 0:         

            multiplos.append(possibilidade)
    
    # Retornando com a lista de múltiplos.
    if negativo == False:
    
        return multiplos
    
    elif negativo == True:

        for item in multiplos:

            multiplos[multiplos.index(item)] = multiplos[multiplos.index(item)] * (-1)
    
    return multiplos
            


def listar_multiplos(lista):      # Essa função lista os items da lista de multiplos, obtida na função acima, verticalmente.
    
    print(f"---> {lista}")
    # Aqui, mostramos uma mensagem caso detectemos que o número é primo.
    if len(lista) == 1 and lista[0] == 1:
        print("\n----> Ou seja: esse é um Número Primo!")

    elif len(lista) == 2 and lista[0] == 1 and lista[1] == entrada_numero:
        print("\n----> Ou seja: é um Número Primo!")

def cabecalho(entrada):
    print(f"------------ {entrada.upper()} ------------\n\nautor: daemon.dev\n\n")
    



# Executando o detector de múltiplos:
    
while True:

    # Cabeçalho:
    
    cabecalho("listar multiplos")

    # I - Capturando o número digitado pelo usuário:

    entrada_numero = input("---> Digite um número inteiro:\n(Esse número não pode ter mais de 8 algarismos, por segurança)\n>>> ")

    # Verificando e transformando ele:

    entrada_numero = transformador_numero_inteiro(entrada_numero)

    # Se o número for negativo == True, iremos fazer essa mudança para mostrar ele certo.
    
    os.system("cls")

    # Faremos esse pequeno ajuste estético para que, caso o número seja negativo, ele apareça da maneira certa no terminal quando forem mostrados os múltiplos.
    if negativo == True:

        print(f"----------------------------------\n\nLista de Múltiplos de [-{entrada_numero}]:\n\n")

    else:

        print(f"----------------------------------\n\nLista de Múltiplos de [{entrada_numero}]:\n\n")

    listar_multiplos(encontrar_multiplo(entrada_numero))
    print("\n\n----------------------------------")

    escolha = input("\nDeseja tentar novamente? 1 - sim e 2 - não.\n>>> ")

    if escolha.startswith("1"):
        os.system("cls")
        negativo = False
    else:
        os.system("cls")
        break

print("\nMuito obrigado! Até logo!")