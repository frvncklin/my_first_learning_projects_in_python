
# ------- Closure -------

import os

def criar_saudacao(saudacao, mensagem):
    def saudar(nome):
        return f'{saudacao}, {nome}. {mensagem}'
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
nome = input("---> Digite seu nome:\n>>> ")
print(f"\nQue horas são {nome}? (Ex: 10:24 ou 18:32)")


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
        print(f"{saudacao_manha(nome)}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    elif 13 <= horas <= 17 and sinalizador == True and minutos <= 59:
        os.system("cls")
        print(cabecalho_programa())
        print(f"{saudacao_tarde(nome)}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    elif 18 <= horas <= 23 and sinalizador == True and minutos <= 59:
        os.system("cls")
        print(cabecalho_programa())
        print(f"{saudacao_noite(nome)}.\n----> São {horario}hrs.")
        print("\nMuito obrigado!")
        break
    else:
        os.system("cls")
        print(cabecalho_programa())
        print(f"Horário inválido.\nVamos tentar novamente!")
