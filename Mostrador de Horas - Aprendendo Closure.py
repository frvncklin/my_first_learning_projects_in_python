
# ------- Closure -------

# def criar_saudacao(saudacao, nome):
#     return f"{saudacao}, {nome}."

# s1 = criar_saudacao("Bom dia", "Victor")
# s2 = criar_saudacao("Bom dia", "Gabi")

# print(s1)
# print(s2)

# def saudacoes_multiplas(mensagem, *args):

#     for argumento in args:
#         print(criar_saudacao(mensagem, argumento))

# saudacoes_multiplas("Bom dia", "Victor", "Gabi", "Fernanda", "Dita", "Beto", "Claudia")

import os

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

def cabecalho(entrada):
    def gerar_cabecalho():
        return f"------------ {entrada.upper()} ------------\n\nautor: daemon.dev\n\n"
    return gerar_cabecalho


# Estou usando closure para salvar o valor dessas diferentes situações da função e armazenando elas em variáveis que serão ativas posteriormente quando eu quiser.
saudacao_manha = criar_saudacao("Bom dia", "que linda manhã!")
saudacao_tarde = criar_saudacao("Boa tarde", "que tarde proveitosa!")
saudacao_noite = criar_saudacao("Boa noite", "que noite relaxante!")
cabecalho_programa = cabecalho("Mostrador de Horário --> Aprendendo Closure")

print(cabecalho_programa())
print("Digite que horas são:")

while True:

    horario = input(">>> ")

    sinalizador = False
    algarismos = ''
    horas = 0
    minutos = 0

    for numero in horario:

        if numero.isdigit() == True:

            algarismos += numero

        if numero == ":" and len(algarismos) == 2:

            horas = int(algarismos)
            algarismos = ''
            sinalizador = True
        
        if sinalizador == True and len(algarismos) == 2:

            minutos = int(algarismos)

            horario_real = f"{horas}:{minutos}"

    if 0 <= horas <= 12 and sinalizador == True and minutos <= 59:
        os.system("cls")
        print(cabecalho_programa())
        print(f"{saudacao_manha()}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    elif 13 <= horas <= 17 and sinalizador == True and minutos <= 59:
        os.system("cls")
        print(cabecalho_programa())
        print(f"{saudacao_tarde()}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    elif 18 <= horas <= 23 and sinalizador == True and minutos <= 59:
        os.system("cls")
        print(cabecalho_programa())
        print(f"{saudacao_noite()}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    else:
        os.system("cls")
        print(cabecalho_programa())
        print(f"Horário inválido.\nVamos tentar novamente!")




        

