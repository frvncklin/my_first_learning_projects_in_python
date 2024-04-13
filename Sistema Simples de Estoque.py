# Este é um sistema de estoque simples que eu desenvolvi.
# A vizaulização dos itens ainda não está boa mas fiz como exercício.


import os

# Criando as funções que iremos utilizar:

# Essa função transforma uma entrada em um número inteiro ou decimal positivo.
def transformador_numero_completo(numero_tranf):

    erros = 0

    while True:

        # ---> Caso o número seja inteiro positivo:

        if numero_tranf.isdigit() == True:

            numero_tranf = int(numero_tranf)
            if erros > 1:
                print("OK! Corrigido.\n")
            return numero_tranf

        # ---> Caso o número seja decimal (ou inválido):

        elif numero_tranf.isdigit() == False:

            # Usaremos esse contador para controlar o número de vírgulas ou pontos. Não pode ter mais de uma.
            contador_ponto_virgula = 0

            # Usaremos esse indice para, no momento da iteração, poder verificar quando o iterador chegou no último dígito do número.
            indice = 0

            # Vamos dar um scan nele, letra por letra.
    
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
                    erros += 1
                    break

                # Se ele chegou até o final da verificação sem dar break e é positivo, então ele pode ser convertido agora.
                if ultimo_caractere == True and e_numero == True:

                    numero_tranf = float(numero_tranf)
                    if erros > 1:
                        print("OK! Corrigido.\n")
                    return numero_tranf
            
                # Caso seja um número negativo, vamos verificar se é inteiro ou não e convertê-lo de acordo.
        
                elif ultimo_caractere == True and e_numero == True:

                    if contador_ponto_virgula >= 1:   # Float.

                        numero_tranf = float(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        return numero_tranf

                    elif contador_ponto_virgula == 0:  # Inteiro

                        numero_tranf = int(numero_tranf) * (-1)
                        if erros > 1:
                            print("OK! Corrigido.\n")
                        return numero_tranf
                
                indice += 1

        # Caso ele saia do "for", então quer dizer que o número é inválido. Vamos criar um loop para que o user corrija:

        if erros == 1:
            print(f"\n---> Você digitou o número inválido [{numero_tranf}] - Por favor corrija-o:")
            numero_tranf = input(">>> ")

        elif erros > 1:
            numero_tranf = input(">>> ")

# Essa função transforma uma entrada str em um número inteiro positivo. Usaremos ela exclusivamente para o cálculo da quantidade dos itens.
def transformador_quantidade(numero_transf):

    if numero_transf.isdigit() == True:
        numero_transf = int(numero_transf)
        return numero_transf
    
    else:
        print("\nEste número é inválido, digite um número válido!")

        while True:
            numero_transf = input(">>> ")
            if numero_transf.isdigit() == True:
                numero_transf = int(numero_transf)
                return numero_transf
            
# Essa função transforma uma entrada str em um número inteiro positivo até um certo limite. Usaremos ela para trabalhar com alguns indices.
def transformador_numero_especifico(numero_transf, limite):

    if numero_transf.isdigit() == True and int(numero_transf) <= limite:
        numero_transf = int(numero_transf)
        return numero_transf
    
    else:
        print("\nEste número é inválido, digite um número válido!")

        while True:
            numero_transf = input(">>> ")
            if numero_transf.isdigit() == True and int(numero_transf) <= limite:
                numero_transf = int(numero_transf)
                return numero_transf

# Essa função mostra nosso cabeçalho.
def cabecalho(entrada):
    def gerar_cabecalho():
        return f"------------ {entrada.upper()} ------------\n\nautor: daemon.dev\n\n"
    return gerar_cabecalho

# ---------------------- SISTEMA SIMPLES DE ESTOQUE ----------------------


estoque = {
    'produto': [],
    'valor_produto': [],
    'quantidade_produto': [],
}

cabecalho_sistema = cabecalho("Sistema Simples de Estoque")

while True:

    # Cabeçalho.
    print(cabecalho_sistema())

    # Menu
    print("----> Menu do Estoque:")
    print("")
    print("(1) - Adicionar Itens ao Estoque.")
    print("(2) - Apagar Itens do Estoque.") 
    print("(3) - Alterar dados dos Itens.")
    print("(4) - Vizualizar estoque.")

    escolha_menu = input("\n>>> ")

    # Submenu: Adicionar Item (1).
    if escolha_menu.startswith("1"):

        os.system("cls")
        print(cabecalho_sistema())
        print("ADICIONAR ITEM (digite \"0\" para sair).")
        print("")

        # ----- Digite o nome do item. ------
        nome = input("-> Digite o nome do(s) item(s): ")

        if nome.startswith("0"):
            os.system("cls")
            continue
        else:
            estoque['produto'].append(nome)
        
        # ----- Digite o valor do item. ------
        valor = input("-> Digite o valor do(s) item(s): ")
        valor = transformador_numero_completo(valor)

        if valor == 0:
            del estoque['produto']['produto'.index(nome)]
            os.system("cls")
            continue
        else:
            estoque["valor_produto"].append(valor)

        # ----- Digite a quantidade do item. ------
        quantidade = input("-> Digite a quantidade do(s) item(s): ")
        quantidade = transformador_quantidade(quantidade)

        if quantidade == 0:
            del estoque['produto']['produto'.index(nome)]
            del estoque['valor_produto']['valor_produto'.index(valor)]
        else:
            estoque['quantidade_produto'].append(quantidade)
        
        os.system("cls")

    # Submenu: Deletar um item (2).
    
    elif escolha_menu.startswith("2"):
        os.system("cls")
        print(cabecalho_sistema())
        i = 0
        for i in range(0, len(estoque['produto'])):

            print(f"[{i + 1}] {estoque['produto'][i]}\t\tR${estoque['valor_produto'][i]}\t\t{estoque['quantidade_produto'][i]}(qtd.)  | Total: R${(estoque['valor_produto'][i]) * (estoque['quantidade_produto'][i]):.2f}")
            
        print("")
        deletar_item = input("Digite o índice do item que deseja deletar:\n>>> ")
        deletar_item = transformador_numero_especifico(deletar_item, len(estoque['produto']))

        del estoque["produto"][deletar_item - 1]
        del estoque['valor_produto'][deletar_item - 1]
        del estoque['quantidade_produto'][deletar_item - 1]
        os.system("cls")

    # Submenu: Alterar os dados de um item (3).
    elif escolha_menu.startswith("3"):
        os.system("cls")
        print(cabecalho_sistema())
        for i in range(0, len(estoque['produto'])):

            print(f"[{i + 1}] {estoque['produto'][i]}\t\tR${estoque['valor_produto'][i]}\t\t{estoque['quantidade_produto'][i]}(qtd.)  | Total: R${(estoque['valor_produto'][i]) * (estoque['quantidade_produto'][i]):.2f}")
        
        print("")
        alterar_item = input("Digite o índice do item que deseja alterar:\n>>> ")
        alterar_item = transformador_numero_especifico(alterar_item, len(estoque['produto']))
        os.system("cls")
        print(cabecalho_sistema())
        print(f"[Item a ser alterado]: [1]{estoque['produto'][alterar_item - 1]}\t\t[2]R${estoque['valor_produto'][alterar_item - 1]}\t\t[3]{estoque['quantidade_produto'][alterar_item - 1]}(qtd.)")
        print("")
        alterar_dado = input("Agora, digite o número do que você deseja alterar:\n>>> ")
        alterar_dado = transformador_numero_especifico(alterar_dado, 3)

        if alterar_dado == 1:
            estoque['produto'][alterar_item - 1] = input("Novo nome -> ")
        elif alterar_dado == 2:
            estoque['valor_produto'][alterar_item - 1] = input("Novo valor -> ")
            estoque['valor_produto'][alterar_item - 1] = transformador_numero_completo(estoque['valor_produto'][alterar_item - 1])
        elif alterar_dado == 3:
            estoque['quantidade_produto'][alterar_item - 1] = input("Nova quantidade -> ")
            estoque['quantidade_produto'][alterar_item - 1] = transformador_quantidade(estoque['quantidade_produto'][alterar_item - 1])
        os.system("cls")


    # Submenu: Vizualizar o estoque (4).
    elif escolha_menu.startswith("4"):
        os.system("cls")
        print(cabecalho_sistema())
        print("ESTOQUE:")
        print("")

        i = 0
        for i in range (0, len(estoque["produto"])):

            print(f"[{i + 1}] {estoque['produto'][i]}\t\tR${estoque['valor_produto'][i]}\t\t{estoque['quantidade_produto'][i]}(qtd.)  | Total: R${(estoque['valor_produto'][i]) * (estoque['quantidade_produto'][i]):.2f}")
            
        print("")
        pausa = input("Pressione enter para continuar.")
        os.system("cls")