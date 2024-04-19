# Definindo as nossas funções:

def organizar_por_nome(item):
    return item['nome']

def mostrar_dicionarios_separadamente_em_listas_de_dicionarios(lista):

    for indice in range(0, len(pessoas)):

        print(f"Dicionário [{indice}]:\n")

        for chave, valor in lista[indice].items():

            print(f"{chave}: {valor}")
        print("\n----------------------\n")

def definir_ordenamento_de_lista(lista):

    chaves = set()

    for indice in range(0, len(lista)):
        for chave in lista[indice].keys():
            chaves.add(chave)
    
    escolher_chave = input(f"---> Digite a chave que deseja usar para ordenar a lista:\nNão esqueça de digitar, sem aspas, exatamente da forma como ela está escrita, caso contrário irá dar erro!\n{chaves}\n>>> ")

    def ordenar(item):
        return item[f'{escolher_chave}']
        
    return ordenar

# Definindo o dicionário que usaremos:

pessoas = [
    {'nome': 'Victor', 'sobrenome': 'Francklin', 'endereco': 'Rua delhi 120'},
    {'nome': 'Gabrielle', 'sobrenome': 'Francklin Souto', 'endereco': 'Rua delhi 120'},
    {'nome': 'Rafael', 'sobrenome': 'Ilbern', 'endereco': 'Florezia 20'},
    {'nome': 'Leonardo', 'sobrenome': 'da Vinci', 'endereco': 'Florezia 30'},
    {'nome': 'Michelangelo', 'sobrenome': 'Antonellini', 'endereco': 'Florezia 46'},
]

# Executando o ordemento:

# I - Mostrando a lista de dicionários que tínhamos.

print("----------- Ordenando Listas de Dicionários --------------\n")
print(f"\nNossa lista de dicionários atual:\n{pessoas}\n\n")

# II - Pedindo ao usuário para escolher, de acordo com as chaves, como o programa vai ordenar a sua lista.
pessoas.sort(key=definir_ordenamento_de_lista(pessoas))
print("\n................Ordenando..................\n")

# III - Exibindo o ordenamento da lista: 

print()
mostrar_dicionarios_separadamente_em_listas_de_dicionarios(pessoas)
