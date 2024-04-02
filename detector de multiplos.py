# Vamos construir um detector de múltiplos, que recebe um número do usuário, mais outro e verifica se eles são múltiplos.
# Após isso, ele mostra os demais números múltiplos daquele número para o usuário, de 1 até ele mesmo.

# Por razões de segurança, limitaremos a 8 algarismos no máximo.


# --------------- Definindo funções que iremos utilizar ------------------:


def verificar_multiplo(numero, multiplo):         # Essa função checa se os parâmetros inseridos são múltiplos.
    if numero % multiplo == 0:
        return True
    else:
        return False
    

def verificador_e_transformador_numero_inteiro(numero):     # Essa função vai verificar e transformar as entradas do usuário em um número inteiro, retornando com ele transformado.


    # Caso o parãmetro seja inteiro, transformar a str de entrada em um int diretamente.
    if numero.isdigit() == True and "." not in numero and len(numero) <= 8:

        numero = int(numero)
        return numero

    # Se não for inteiro e/ou tiver mais de 8 algarismos, criar um loop que será quebrado assim que o usuário digitar um número inteiro válido.
    else:       

        print("\nVocê digitou um número inválido, tente novamente!\n")

        while True: 

            numero = input(">>> ")

            # Quando o número digitado for válido, convertê-lo e quebrar o loop.
            if numero.isdigit() == True and "." not in numero:
                numero = int(numero)
                print("Ok! Corrigido!\n")
                break

        # Assim que o número for válido e convertido, retornar com ele
        return numero
    
    
def encontrar_verdadeiro_multiplo(numero):      # Essa função encontra todos os número múltiplos do parâmetro escolhido, a partir de 1.

    # Criando a lista para colocar os múltiplos do numero.
    verdadeiros_multiplos = []

    # Percorrendo todos os possíveis múltiplos do numero.
    for possibilidade in range(1, numero + 1):         

        # Capturando os números que são múltiplos do número.
        if numero % possibilidade == 0:         

            verdadeiros_multiplos.append(possibilidade)
    
    # Retornando com a lista de múltiplos.
    return verdadeiros_multiplos


def listar_multiplos(lista):      # Essa função lista os items da lista de multiplos, obtida na função acima, verticalmente.

    for item in lista:
        print(f"-> {item}")
    
    # Aqui, mostramos uma mensagem caso detectemos que o número é primo.
    if len(lista) == 1 and lista[0] == 1:
        print("\n----> Ou seja: esse é um Número Primo!")

    elif len(lista) == 2 and lista[0] == 1 and lista[1] == entrada_numero:
        print("\n----> Ou seja: é um Número Primo!")




# Executando o detector de múltiplos:
    

# Cabeçalho:
    
print("------------ DETECTOR DE MÚLTIPLOS ------------\n\nautor: daemon.dev\n\n")


# Capturando as entradas do usuário:


# I - Capturando o primeiro número:

entrada_numero = input("---> Digite um número inteiro:\n(Esse número não pode ter mais de 8 algarismos, por segurança)\n>>> ")

# -->  Verificando se o número digitado é válido e o corrigindo.

entrada_numero = verificador_e_transformador_numero_inteiro(entrada_numero)


# II - Capturando o múltiplo (segundo número):

entrada_multiplo = input("\n---> Digite o número inteiro que você quer verficar se é multiplo deste (mesma regra):\n>>> ")

# --> Verificando se ele é válido e o corrigindo se necessário.

entrada_multiplo = verificador_e_transformador_numero_inteiro(entrada_multiplo)


# III - Aplicando a função múltiplo para verificar se os números digitados são múltiplos.

e_multiplo = verificar_multiplo(entrada_numero, entrada_multiplo) == True
nao_e_multiplo = verificar_multiplo(entrada_numero, entrada_multiplo) == False

# Caso forem, exibir uma mensagem informando que houve sucesso e seus demais múltiplos entre 1 e 1000.
if e_multiplo: 

    print("\n-------------------------------\n")
    print(f"Parabéns!!\n=> {entrada_numero} é múltiplo de {entrada_multiplo}.")
    numeros_multiplos = encontrar_verdadeiro_multiplo(entrada_numero)
    print(f"\nEstes são todos os seus múltiplos:\n")
    listar_multiplos(numeros_multiplos)

# Caso não forem, exibir uma mensagem informando que não houve sucesso e utilizar a função "encontrar_verdadeiro_multiplo()" 
# para encontrar os possíveis múltiplos para esse número entre 1 e 1000.
elif nao_e_multiplo: 

    print("\n--------------------------------\n")
    numeros_multiplos = encontrar_verdadeiro_multiplo(entrada_numero)

    print(f"Infelizmente... {entrada_numero} não é multiplo de {entrada_multiplo} :( .\n\nE sim de:")
    listar_multiplos(numeros_multiplos)

print("\nObrigado!\n\n------------ENCERRADO------------")