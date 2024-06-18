"""
Exercício de soma de listas:

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]

"""
def decorator(param):
    print(f"Decorator Parameter: {param}")
    def function_fabric(func):
        print(f"Saving Function ---> {func.__name__}")
        def nested_function(*args, **kwargs):
            res = func(*args, *kwargs)
            return res
        print("Function saved!")
        return nested_function
    return function_fabric

@decorator("First")
def list_sum(l1, l2):
    max_lengh = min(len(l1), len(l2))
    new_list = [(l1[i] + l2[i]) for i in range(max_lengh)]
    return new_list

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_ab = list_sum(lista_a, lista_b)

print(lista_ab)

# by kvtana