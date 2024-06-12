# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Resolvendo o exercício:

def decorator_fabric(name):
    print(f'{name}', end=' ')
    def function_fabric(func):
        print(f'---> Saving function: {func.__name__}')

        def nested_function(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        print("Function saved!")
        return nested_function
    return function_fabric

@decorator_fabric("First")
def list_zipper(list1, list2):

    # Use the lowest number of indexes.
    max_index = len(list1) if len(list1) <= len(list2) else len(list2)

    new_list = [(list1[index], list2[index]) for index in range(max_index)]
    
    return new_list

lista_01 = ['Salvador', 'Bahia', 'Belo Horizonte']
lista_02 = ['BA', 'SP', 'MG', 'RJ']

list_union = list_zipper(lista_01, lista_02)

print(list_union)

# by kvtana