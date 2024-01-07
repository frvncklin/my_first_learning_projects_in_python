frase = " O phyton é uma linguagem de programação multiparadigma. Phyton foi criado por Guido Van Rossun"
print(f"Vamos analisar essa frase: \"{frase}\".\nNossa missão é descobrir o a letra que mais se repete nessa frase.")

i = 0
lista_letras = []
lista_repeticao = []

frase = frase.replace(" ", "")  # Retirando os espaços, para que eles não interfiram em nossa análise.

while i < len(frase):
    lista_letras.append(frase[i])
    lista_repeticao.append(frase.count(frase[i]))

    i += 1

    # Criei um loop para armazenar nos valores das letras e da quantidade de vezess que elas aparecem. Depois disso, vou cruzar elas
    # para descobrir qual é a letra que mais aparece.

posicao_maior = lista_repeticao.index(max(lista_repeticao))
letra_maior = lista_letras[posicao_maior]
print(f"\nColocamos nossa máquina para processar!\n......................\nA letra que mais aparece nessa frase é: \"{lista_letras[posicao_maior]}\" !")

