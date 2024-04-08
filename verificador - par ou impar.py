import os

# Determinando as funções que iremos utilizar:

# FUNÇÃO 1 --> Transformar entrada do usuário "str" em número e crorrigí-la se for inválida.

def transformador_numero(numero_tranf):

    erros = 0

    while True:

        # ---> Caso o número seja inteiro positivo:

        if numero_tranf.isdigit() == True:

            numero_tranf = int(numero_tranf)
            if erros > 1:
                print("OK! Corrigido.\n")
            os.system("cls")
            return numero_tranf

        # ---> Caso o número seja decimal (ou inválido):

        elif numero_tranf.isdigit() == False:

            # Usaremos esse contador para controlar o número de vírgulas ou pontos. Não pode ter mais de uma.
            contador_ponto_virgula = 0

            # Usaremos esse indice para, no momento da iteração, poder verificar quando o iterador chegou no último dígito do número.
            indice = 0

            # Se ele começar com um tracinho, isso isgnifica que é [NEGATIVO]. Vamos tomar nota disso negativo usando a variável global booleana *negativo*.
            if numero_tranf.startswith("-"):

                numero_tranf = numero_tranf.replace("-", "")
                global negativo
                negativo = True

            # Depois de verificar o tracinho inicial, vamos dar um scan nele, letra por letra.
    
            for digito in numero_tranf:

                e_numero = digito.isdigit() == True
                e_virgula = digito == ","
                e_ponto = digito == "."
                invalido = e_numero == False and e_virgula == False and e_ponto == False
                ultimo_caractere = indice == len(numero_tranf) - 1

                # Se for uma vígula, transforma em ponto e continua.
                if e_virgula:

                    numero_tranf = numero_tranf.replace(",", ".")
                    contador_ponto_virgula += 1
                
                # Se for um ponto, continua.
                elif e_ponto:
                    contador_ponto_virgula += 1
                    continue
                
                # Se tiver mais de um ponto ou vírgula, para.
                if contador_ponto_virgula > 1:
                    erros += 1
                    break

                # Se for um número inválido, vai retornar a str original, fato que usaremos para fazer uma correção mais tarde.
                if invalido:
                    # É importante eu corrgir o "negativo" caso o número for inválido pois isso evitará problemas de conversão 
                    # nas futuras correções do usuário. Pois o usuário pode digitar, por exemplo "-absnak" e isso, se não
                    # corrigirmos, ficará registrado como número negativo, o que irá afetar as novas entradas do usuário, mesmo
                    # se elas forem números válidos.
                    negativo = False
                    erros += 1
                    break

                # Se ele chegou até o final da verificação sem dar break e é positivo, então ele pode ser convertido agora.
                if ultimo_caractere == True and e_numero == True and negativo == False:

                    numero_tranf = float(numero_tranf)
                    if erros > 1:
                        print("OK! Corrigido.\n")
                    os.system("cls")
                    return numero_tranf
            
                # Caso seja um número negativo, vamos verificar se é inteiro ou não e convertê-lo de acordo.
        
                elif ultimo_caractere == True and e_numero == True and negativo == True:

                    if contador_ponto_virgula >= 1:   # Float.

                        numero_tranf = float(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        os.system("cls")
                        return numero_tranf

                    elif contador_ponto_virgula == 0:  # Inteiro

                        numero_tranf = int(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        os.system("cls")
                        return numero_tranf
                
                indice += 1

        # Caso ele saia do "for", então quer dizer que o número é inválido. Vamos criar um loop para que o user corrija:

        if erros == 1:
            print(f"\n---> Você digitou o número inválido [{numero_tranf}] - Por favor corrija-o:", end="")
            numero_tranf = input("\n>>> ")

        elif erros > 1:
            numero_tranf = input(">>> ")

# FUNÇÃO 2 ---> Determina se o número é par ou ímpar.
            
def determinador_par_impar(numero):

    par = numero % 2 == 0
    impar = numero % 3 == 0
    primo = numero % 2 != 0 and numero % 3 != 0

    if par:
        mensagem = f"----> O número {numero} é PAR."
        return mensagem
    if impar:
        mensagem = f"----> O número {numero} é ÍMPAR."
        return mensagem
    if primo:
        mensagem = f"----> O número {numero} é PRIMO."
        return mensagem

# FUNÇÃO 3 ---> Cria do design do nosso cabeçalho.
        
def cabecalho(entrada):
    titulo = print(f"------------ {entrada.upper()} ------------\n\nautor: daemon.dev\n\n")
    return titulo

# ----------------------------------------------

# Vamos ao programa!



while True:

    # Cabeçalho.

    cabecalho("É par ou ímpar?")
    print("Este programa verifica se um número é par ou ímpar!")

    # Recebendo entrada do usuário e transformando-a em número.
    
    entrada_numero = input("\nDigite o número que quer testar:\n>>> ")
    entrada_numero = transformador_numero(entrada_numero)

    # Determinando se ele é par ou ímpar

    print(f"\n{determinador_par_impar(entrada_numero)}")

    escolha = input("\nDeseja tentar novamente? 1 - sim e 2 - não.\n>>> ")

    if escolha.startswith("1"):
        os.system("cls")
    else:
        os.system("cls")
        print("\nMuito obrigado! Até logo!")