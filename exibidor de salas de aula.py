# Lista de listas e seus indices.

salas = [
    # 0         1
    ['Maria', 'Helena', ],          # 0
    # 0
    ['Gabrielle', ],                # 1
    # 0         1         2
    ['Luis', 'Miguel', 'João',]  # 2
]

# Para acessar os valores de listas dentro de listas, basta digitar a sequencia correta de indices.
 
print("Listagem de alunos por salas:\n")
for sala in salas:
    print(f'Sala {salas.index(sala)}:\n')
    for aluno in sala:
        print(f'--> {aluno}')
    print("\n----------------\n")
# é importante que os itens de uma lista sejam de um mesmo tipo para que não tenhamos que ficar fazendo uns IFs malucos
