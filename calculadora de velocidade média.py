# Definindo a função "Transformador de Número", que irá transformar a entrada propriamente em um int ou float.

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
        
# Definindo a função de cálculo da Velocidade Média.

def velocidade_media(distancia, tempo):
    velocidade_media = distancia / tempo
    print(f"----> Sua velocidade média é: {velocidade_media:.2f} km\\h")

# Executando o programa.

print("------------ CALCULADORA DE VELOCIDADE MÉDIA ------------\n\nautor: daemon.dev\n\n")

# Capturando as entradas de distãncia e tempo.

entrada_distancia = input("Digite a distância (em km):\n>>> ")
entrada_tempo = input("Agora, o tempo (em h):\n>>> ")

# Aplicando as entradas no transformador.

entrada_distancia = transformador_numero(numero_tranf=entrada_distancia)
entrada_tempo = transformador_numero(numero_tranf=entrada_tempo)

# Aplicando a função de cálculo da Velocidade Média.

velocidade_media(distancia=entrada_distancia, tempo=entrada_tempo)


# Lembrar! Funções tem memória curta ! Elas não guardam valores nem os alteram permanentemente.
# Você precisa usar return para voltar com os valores alterados, caso contrário eles retornarão NoneType.