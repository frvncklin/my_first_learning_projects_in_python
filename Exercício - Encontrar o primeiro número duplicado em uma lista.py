def encontrar_primeira_duplicata(lista):

    duplicata = -1
    sacola_de_numeros = set()

    for numero in lista:
        if numero in sacola_de_numeros:
            duplicata = numero
            break

        sacola_de_numeros.add(numero)
    
    return duplicata

# Nesta função, ele vai iterar sobre uma lista e ir jogando os números 
# iterados em uma sacola de números (que é o nosso set).
# Cada vez que ele joga, ele verifica se o número que ele jogou tem
# outro igual dentro da sacola.
# Assim que ele for jogar um número e ver que já tem outro igual na
# sacola, ele irá quebrar o ciclo e retornar esse número pra gente.
# Este número é a primeira duplicata da lista que estávamos querendo
# achar. :)
# --> Caso não haja duplicatas, ele irá retornar [-1].
    
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for lista in lista_de_listas_de_inteiros:
    print(f"{lista} ---> {encontrar_primeira_duplicata(lista)}")

# autor: kvtana (former daemon.dev)