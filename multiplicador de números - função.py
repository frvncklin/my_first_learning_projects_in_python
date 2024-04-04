# ---------- Multiplicador de Números -------------

# Definindo função do muntiplicador

def multiplicador(*args):
    produto = 1
    for numero in args:
        produto *= numero
    return produto

# Definindo função de transformar a entrada em um número int ou float.

def transformador_str_numero(numero_transf):

    if numero_transf.isdigit() == True:

        numero_transf = int(numero_transf)
        return numero_transf

    elif numero_transf.isdigit() == False:

        if "." in numero_transf:

            try:
                numero_transf = float(numero_transf)
                return numero_transf
            except:
                return numero_transf    # Acontece quando o número digitado tem uma letra e um ponto (ex: 3a.a ou ab.2). Nesse caso vamos retornar com a str inalterada e trataremos o erro depois.
        
        # elif "," in numero_transf:

        #     numero_transf.replace(",", ".")

        #     try:
        #         numero_transf = float(numero_transf)
        #         return numero_transf
        #     except:
        #         return numero_transf    
        
        else:
            return numero_transf    # Acontece quando o número digitado tem uma letra. Nusse caso, retornamos com a str inalterada e iremos tratar esse erro depois



entrada_numeros = input("-> Digite os números que você deseja multiplicar:\n\n-------------Regrinhas-------------\n\n(Separe eles por vírgulas. Ex: 1, 30, 40, 50 == 1 * 30 * 40 * 50)\n(Caso queira colocar um múmero decimal, escreva ele com ponto \".\" --> Ex: 19.98 \n-------------------------------\n\n>>> ")

entrada_numeros = entrada_numeros.split(",")

# Transformando os números digitados pelo usuário em int e float:

for indice, numero in enumerate(entrada_numeros):
    entrada_numeros[indice] = entrada_numeros[indice].strip()
    entrada_numeros[indice] = transformador_str_numero(entrada_numeros[indice])

    # Caso o número seja inválido, faremos o usuário o corrigir, criando um loop no qual ele vai inserir valores até que seja um válido para o número. Então iremos converter o numero em float ou int usando a função e continuar.
    if type(entrada_numeros[indice]) == str:    # Deixei o transformafor retornar o valor de str original de propósito caso ele não conseguisse converter, para que pudéssemos detectar e corrigir agora.
        print(f"\n(!)Detectamos um erro no número [{entrada_numeros[indice]}]. Por favor corrija-o:", end="")
        while True:
            entrada_numeros[indice] = input("\n>>> ")

            if type(transformador_str_numero(entrada_numeros[indice])) != str:
                entrada_numeros[indice] = transformador_str_numero(entrada_numeros[indice])
                break

# Realizando o produto, usando a função multiplicador:

print(f"\n\n-----> O produto total será: {multiplicador(*entrada_numeros):.2f}")