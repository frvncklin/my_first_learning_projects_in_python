def transformador_numero(numero_tranf):

    erros = 0

    while True:

        # ---> Caso o número seja inteiro positivo:

        if numero_tranf.isdigit() == True:

            numero_tranf = int(numero_tranf)
            if erros > 1:
                print("OK! Corrigido.\n")
            # os.system("cls")
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
                    # os.system("cls")
                    return numero_tranf
            
                # Caso seja um número negativo, vamos verificar se é inteiro ou não e convertê-lo de acordo.
        
                elif ultimo_caractere == True and e_numero == True and negativo == True:

                    if contador_ponto_virgula >= 1:   # Float.

                        numero_tranf = float(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        # os.system("cls")
                        return numero_tranf

                    elif contador_ponto_virgula == 0:  # Inteiro

                        numero_tranf = int(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        # os.system("cls")
                        return numero_tranf
                
                indice += 1

        # Caso ele saia do "for", então quer dizer que o número é inválido. Vamos criar um loop para que o user corrija:

        if erros == 1:
            print(f"\n---> Você digitou o número inválido [{numero_tranf}] - Por favor corrija-o:", end="")
            numero_tranf = input("\n>>> ")

        elif erros > 1:
            numero_tranf = input(">>> ")

def fazer_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

def tratamento_string_separada_por_virgulas(string):

    string = string.split(",")

    for item in string:
        string[string.index(item)] = string[string.index(item)].strip()
    
    return string

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

    
duplicar = fazer_multiplicacao(2)
triplicar = fazer_multiplicacao(3)
quadruplicar = fazer_multiplicacao(4)

entrada_numero = input("----> Digite um número:\n>>> ")

entrada_numero = transformador_numero(entrada_numero)

escolha_usuario = input("\nDeseja?\n\n------------------\n1 - Duplicar\n2 - Triplicar\n3 - Quaduplicar\n------------------\n\n>>> ")

if "1" in escolha_usuario:
    entrada_numero = duplicar(entrada_numero)
elif "2" in escolha_usuario:
    entrada_numero = triplicar(entrada_numero)
elif "3" in escolha_usuario:
    entrada_numero = quadruplicar(entrada_numero)
    entrada_numero = duplicar(entrada_numero)
    entrada_numero = triplicar(entrada_numero)
    entrada_numero = quadruplicar(entrada_numero)

print(f"\n=> O resultado final é: {entrada_numero}.")

entrada_nomes_saudacao = input("\n----> Agora, nos diga para que deseja enviar uma saudação (separe por vírgulas, ex: Victor, Gabi, Beto, Claudia):\n>>> ")

entrada_nomes_saudacao = tratamento_string_separada_por_virgulas(entrada_nomes_saudacao)

entrada_escolha_saudacao = input("\nEscolha: 1 - Bom dia, 2 - Boa noite.")

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

if entrada_escolha_saudacao.startswith("1"):

    for nome in entrada_nomes_saudacao:
        print(falar_bom_dia(nome))

elif entrada_escolha_saudacao.startswith("2"):

    for nome in entrada_nomes_saudacao:
        print(falar_boa_noite(nome))

else:
    print("Tchau!")