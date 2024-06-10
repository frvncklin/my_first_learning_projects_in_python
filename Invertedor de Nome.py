def inverte_string(string):
    string = string.lower()
    nova_string = ''
    indice = 0

    for letra in string:
        
        inserir_maiuscula = False

        if indice < len(string) - 1 and string[indice + 1] == " ": # Caso a letra seguinte seja espaço, torná-la maiúscula.
        # É importnate, aqui, enfatizar que o indice tem que ser menor do que seu valor máximo para não dar erro de Index Out of Range.
            inserir_maiuscula = True
        elif indice == len(string) - 1: # Caso estejamos na última letra da frase, inserir maiúscula também.
            inserir_maiuscula = True
        else:
            inserir_maiuscula = False
        
        if inserir_maiuscula == True:
            nova_string += letra.upper()
        elif inserir_maiuscula == False:
            nova_string += letra

        indice += 1

    string = nova_string
    return string[::-1]

while True:

    print("------------ INVERTEDOR DE NOMES ------------\n\nautor: daemon.dev\n")
    name = input("Digite seu nome completo:\n>>> ")
    inversed_name = inverte_string(name)
    print("\nSeu nome invertido é:", inversed_name)
    print("\n-----------------------------------\n\n")
    escolha = input("Deseja continuar? 1 - sim ou 2 - não\n>>> ")
    if escolha.startswith("1"):
        continue
    else:
        break
print("\n\nObrigado por usar o nosso app!\nAutor: Otuos Elleirbag\n_________________________________________________")