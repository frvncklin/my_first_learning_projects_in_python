lista = []
lista_erros = []
removiveis = []
count = 0
item = ''
verificador = ''       
verificador_alt = ''
remover_unico = ''
contador_erros = 0

import os

print("BEM VINDO A SUA LISTA DE COMPRAS SIMPLES!\n\tCortesia da daemon.dev")
nome_lista = input("\nColoque um nome na sua lista.\n>>> ")
print("")

# Menu.

while True:

    print("------------------------------")
    print("             MENU             ")
    print("------------------------------")
    opcao_menu = input("\n1 - Vizualizar Lista\n2 - Adicionar item\n3 - Apagar item\n4 - Alterar nome da Lista\n\nSelecione uma opção >>> ")

# Vizualizar lista.
    
    if opcao_menu == "1":
    
        print('')

        if len(lista) == 0:

            print("A lista está vazia!\n")
        
        else:
            os.system('cls')
            print(f'\t{nome_lista.upper()}:')
            print(f'\t', "-" * (len(nome_lista) - 1))

            for item in enumerate(lista, start=1):

                indice, nome = item
                print(f'{indice} --> {nome}')

            print('------------')
            print('')

# Opção de continuar ou não.
        
        escolha_continuar = input('Continuar - 1 ou sair - 2. \n>>> ')
        if escolha_continuar.startswith("1"):
            os.system("cls")
            print('')
            continue
        else:
            break

# Adicionar item à lista.
        
    elif opcao_menu == "2":
        os.system('cls')
        adicao = input('\n- Digite o item que deseja adicionar à lista \nSe você separa por vírgulas, adicionaremos mais de um!\n(Ex: Sabonete, biscoito, arroz)\n\n>>> ').lower()
        item = ''
        verificador = ''

        # Diferenciando quando tem vários itens
        if "," in adicao:

            for letra in adicao:
                # Vai iterar a nossa lista de itens para adicionar.
                verificador += letra

                if letra == ",":        # Separando item por item.
                    item = verificador.replace(",", '')      # Eliminando a vírgula deste item.

                    if item.startswith(" "):    # Eliminando o espaço, caso a pessoa digite os itens após as vírgulas pulando espaços.

                        for letra_item in item:

                            count += 1

                            if count > 1:
                                verificador_alt += letra_item

                        item = verificador_alt
                        verificador_alt = ''
                        count = 0

                    lista.append(item)  # Capturando o item para a lista.
                    item = ''           # Resetando o valor do tem e do verificador para capturar o próximo item.
                    verificador = ''

        # Fora do for, irei pegar o último item:
            if verificador.startswith(" "):     #Eliminando o espaço do último item.

                for letra_item_final in verificador:

                    count += 1

                    if count > 1:
                        verificador_alt += letra_item_final
                
                verificador = verificador_alt
                verificador_alt = ''
                count = 0

            lista.append(verificador)
            verificador = ''    # Resetando o valor do verificador e, consequetemente, do último item.

        # Caso a pessoa digite apenas um item, capturar esse item.
        else:   
            if adicao.startswith(" "):

                for letra_item_unico in adicao:

                    count += 1

                    if count > 1:
                        verificador_alt += letra_item_unico
                
                adicao = verificador_alt
                verificador_alt = ''
                count = 0

            lista.append(adicao)


        print("")

        escolha_continuar = input('Continuar - 1 ou sair - 2. \n>>> ')
        if escolha_continuar.startswith("1"):
            print('')
            os.system("cls")
            continue
        else:
            break

# Remover item da lista.
        
    elif opcao_menu == "3": 

        # Visualizando a lista para escolher os itens que quer remover.

        print('')
        os.system('cls')
        print(f'\t{nome_lista.upper()}:')
        print(f'\t', "-" * (len(nome_lista) - 1))

        for item in enumerate(lista, start=1):

            indice, nome = item
            print(f'{indice} --> {nome}')

        print('------------')
        print('')

        remover = input('\n- Digite o(s) item(s) que deseja remover da lista (nome ou indice).\nSe você separar por vírgulas, removeremos mais de um!\n(Ex: arroz, feijão, salada, 2, 3)\n\n>>> ').lower()
        # item = ''
        # verificador = ''       # Detalhe estético.
        # verificador_alt = ''
        # contador_erros = 0

        # Diferenciando quando tem vários itens.
        if "," in remover:

            for letra_remover in remover:
                # Vai iterar os itens que listei para remover.
                verificador += letra_remover

                if letra_remover == ",":        # Separando item por item.

                    item_remover = verificador.replace(",", '')     # Eliminando a vírgula deste item.

                    if item_remover.startswith(" "):                # Eliminando o espaço, caso a pessoa digite os itens após as vírgulas pulando espaços.

                        for letra_item in item_remover:
                            
                            count += 1

                            if count > 1:
                                verificador_alt += letra_item
                            
                        item_remover = verificador_alt
                        verificador_alt = ''
                        count = 0

                    if item_remover.isdigit() == True:
                        
                        item_remover_int = int(f"{item_remover}") - 1       # Estou fazendo isso pois, no enumerate, os indicies estão aparecendo para o usuário somados de 1, então farei isso para não ocorrer erros nos indices.

                        if item_remover_int + 1 <= len(lista):      # Verificando se o índice está na lista.
                                removiveis.append(lista[item_remover_int])
                        
                        elif item_remover_int + 1 > len(lista):     # Caso o indice não esteja na lista.
                            contador_erros += 1
                            lista_erros.append(f"índice inexistente digitado: [{item_remover}]")

                        item_remover_int = 0

                    else:
        
                        if item_remover in lista:   # Removendo item da lista caso esteja nela.
                            removiveis.append(item_remover)

                        elif item_remover not in lista: #Caso o item  não esteja na lista, tomando nota disso em nosso contador de erros.
                            contador_erros += 1
                            lista_erros.append(item_remover)
                    
                    item_remover = ''       # Após capturar ou rejeitar o item, ele vai resetar os valores do verificador e do item.
                    verificador = ''
            
        #Fora do for, verificando o último item:
            
            if verificador.startswith(" "):     #Eliminando o espaço inicial do último item caso haja.

                for letra_item_final in verificador:

                    count += 1

                    if count > 1:
                        verificador_alt += letra_item_final
                
                verificador = verificador_alt   # Espaço eliminado.
                verificador_alt = ''
                count = 0

            if verificador.isdigit() == True:

                
                verificador_int = int(f"{verificador}") - 1     # índice real.

                if verificador_int + 1 <= len(lista):
                    removiveis.append(lista[verificador_int])

                elif verificador_int + 1 > len(lista):
                    contador_erros += 1
                    lista_erros.append(f"índice inexistente digitado: [{verificador}]")     #índice visto pelo usuário.

                verificador_int = 0
                verificador = ''

            else:

                if verificador in lista:
                    removiveis.append(verificador)
                    verificador = ''    # Resetando o valor do verificador e, consequetemente, do último item.

                elif verificador not in lista:
                    contador_erros += 1
                    lista_erros.append(verificador)
                    verificador = ''

            if contador_erros > 0:
                print(f"\nOs seguintes items não estavam na lista: {lista_erros}. Totalizando {contador_erros} erros.")
                contador_erros = 0
                lista_erros = []

            for item_removiveis in removiveis:      # Eliminando os itens identificados da lista.
                if item_removiveis in lista:
                    lista.remove(item_removiveis)
            
            if len(removiveis) > 0:
                print("\nItens removidos com sucesso!")
                removiveis = []

        else:   # Caso seja apenas um item.

            if remover.startswith(" "):
                for letra_remover_unico in remover:

                     count += 1

                     if count > 1:
                        remover_unico += letra_remover_unico

                remover = remover_unico
                remover_unico = ''
                count = 0

            if remover.isdigit() == True:

                remover_int = int(f"{remover}") - 1

                if remover_int + 1 <= len(lista):
                    removiveis.append(lista[remover_int])
                
                else:
                    contador_erros += 1
                    lista_erros.append(f"índice inexistente digitado: [{remover}]")

                remover_unico_int = 0
                remover = ''
            
            else:        # Quando é digitado um único item.

                if remover in lista:
                    removiveis.append(remover)
                    remover = ''
                
                elif remover not in lista:
                    contador_erros += 1
                    lista_erros.append(remover)

            if contador_erros > 0:
                print(f"\nOs seguintes items não estavam na lista: {lista_erros}. Totalizando {contador_erros} erros.")
                contador_erros = 0
                lista_erros = []
            
            for item_removiveis in removiveis:      # Eliminando os itens identificados da lista.
                if item_removiveis in lista:
                    lista.remove(item_removiveis)
            
            if len(removiveis) > 0:
                print("\nItens removidos com sucesso!")
                removiveis = []
          
        print("")

        escolha_continuar = input('Continuar - 1 ou sair - 2. \n>>> ')
        if escolha_continuar.startswith("1"):
            os.system("cls")
            print('')
            continue
        else:
            break

    elif opcao_menu == '4':
        
        print('')
        nome_lista = input("Digite o novo nome da lista:\n>>> ")
        print('')
        os.system("cls")
        print("Nome alterado!\n")
# Caso o usuário digite uma opção inválida:
    else:
        print("\nPor favor digite uma opção válida!\n")
