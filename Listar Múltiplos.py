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
        return numero

    # Se não for inteiro positivo, criar um loop que será quebrado assim que o usuário digitar um número inteiro válido.
    if numero.isdigit() == False:      

        # Se ele for um inteiro negativo:
        if numero.startswith("-"):
            
            # Sinalizar que ele é negativo, utilizando a variável "negativo".
            negativo = True
            numero = numero[1:]

            # Convertê-lo e retornar o valor, com a variável "negativo" == True

            if numero.isdigit() == True:

                numero = int(numero)
                return numero
        
        # Se não for inteiro negativo, neste caso é inválido, então entramos no loop.

        print("\nOps! -> Você digitou um número inválido, tente novamente! Apenas inteiros:")

        while True: 

            negativo = False
            numero = input(">>> ")
            # Quando o número digitado for válido, convertê-lo e quebrar o loop.
            if numero.isdigit() == True:

                numero = int(numero)
                return numero

            elif numero.isdigit() == False:

                if numero.startswith("-"):

                    negativo == True
                    numero = numero[1:]

                    if numero.isdigit() == True:

                        numero = int(numero)
                        return numero
                        
                else: 
                    continue
                
            

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

    # Definindo nosso gerador de múltiplos.
    def encontrar_multiplo(n=0, maximum=entrada_numero): 
        while True:
            
            if n == entrada_numero:
                break

            n += 1
            if entrada_numero % n == 0:
                yield n
            
    # Colocando nosso gerador de múltiplos em uma variável para ativação.
    gen_multiplos = encontrar_multiplo()
    os.system("cls")

    # Faremos esse pequeno ajuste estético para que, caso o número seja negativo, ele apareça da maneira certa no terminal quando forem mostrados os múltiplos.
    if negativo == True:

        print(f"----------------------------------\n\nLista de Múltiplos de [{entrada_numero * -1}]:\n\n")

    elif negativo == False:

        print(f"----------------------------------\n\nLista de Múltiplos de [{entrada_numero}]:\n\n")

# Printando os múltiplos gerados.
    for n in encontrar_multiplo():

        if negativo == False:
            print(f'---> {n}')
        elif negativo == True:
            n *= -1
            print(f'---> {n}')

    print("\n\n----------------------------------")

    escolha = input("\nDeseja tentar novamente? 1 - sim e 2 - não.\n>>> ")

    if escolha.startswith("1"):
        os.system("cls")
        negativo = False
    else:
        os.system("cls")
        break

print("\nMuito obrigado! Até logo!")