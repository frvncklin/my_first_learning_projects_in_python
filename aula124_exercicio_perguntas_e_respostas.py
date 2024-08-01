# Exercício - sistema de perguntas e respostas

def str_to_int(number):
    while True:
        try:
            number = int(number)
            return number
        except:
            number = input('Invalid number, type a valid one: ')

def check_range(number, range_limit):
    while True:

        if number in range(range_limit):
            return number
        
        number = input('Incorrect number, type a valid one (not in the range): ')
        number = str_to_int(number)

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

import os, time

acertos = 0

for pergunta in perguntas:

    for chave, valor in pergunta.items():

        if chave == 'Opções':   # Printing options.
            qtd_opcoes = len(perguntas[perguntas.index(pergunta)]['Opções'])
            for i in range(qtd_opcoes):
                opcao = perguntas[perguntas.index(pergunta)]['Opções'][i]
                print(f'{i}) {opcao}')
            continue

        elif chave == 'Resposta': # Recieving answer from user.
            escolha_user = input('\nDigite sua resposta: ')
            escolha_user = str_to_int(escolha_user)     # Checking if the user's answer is a valid number (int). If not, applying correction.
            escolha_user = check_range(escolha_user, qtd_opcoes)    # Checking if the user's answer is in the range. If not, applying correction.
            resposta_user = perguntas[perguntas.index(pergunta)]['Opções'][escolha_user]
            resposta_correta = perguntas[perguntas.index(pergunta)]['Resposta'] 
    
            if resposta_user == resposta_correta:
                print()
                print("---> Correto!")
                acertos += 1
            else:
                print()
                print("---> Errou...")
            print()
            print('----------------------')
            print()
            continue
            
        print(f'{chave}: {valor}')

print('...............processando...............')
time.sleep(5)
os.system('cls')

# Displaying customized message according to the user's responses.
if acertos == len(perguntas):
    print('Parabéns! Você acertou todas as perguntas!')
elif len(perguntas) / 2 <= acertos < len(perguntas):
    print(f'Parabéns! Você acertou {acertos} respostas.\nRestam apenas {(len(perguntas) - acertos)}!')
elif acertos == 0:
    print(f'Não desista! Todo mundo começa de algum lugar.\nVocê não acertou nenhuma pergunta... mas eu também já estive em seu lugar.\n\nNão abaixe a cabeça e siga em frente, pois você vai conseguir!')
else:
    print(f'Que pena! Você acertou {acertos} perguntas...\nNão desista! Você precisa acertar mais {len(perguntas) - acertos}.')

# Essa solução é escalável. Se você quiser fazer isso com o seu questionário.
# This solution is scalable. If you may wish, you can do it with your own questionary.

# by kvtana
