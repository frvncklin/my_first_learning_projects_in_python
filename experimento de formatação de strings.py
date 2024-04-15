nome = 'Victor Francklin'
tamanho_nome = len(nome)

indice = 1
nova_string = nome[0]
meio_do_nome = (nome.find(" "), nome.find(" ") + 1)

while indice < tamanho_nome:
    if indice in meio_do_nome:
        nova_string += nome[indice]
    else:
        nova_string += '*' + nome[indice]
    indice += 1

print(f'{nova_string:-^50}')
