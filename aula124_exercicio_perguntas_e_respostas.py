# Exercício - sistema de perguntas e respostas


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

import os

acertos = 0

for pergunta in perguntas:

    for chave, valor in pergunta.items():

        if chave == 'Resposta':
            resposta = input('\nDigite sua resposta: ')
            acertos += 1 if resposta == perguntas[perguntas.index(pergunta)]['Resposta'] else 0
            print()
            print('----------------------')
            print()
            continue
            
        print(f'{chave}: {valor}')

os.system('cls')

if acertos == len(perguntas):
    print('Parabéns! Você acertou todas as perguntas!')
elif len(perguntas) / 2 <= acertos < len(perguntas):
    print(f'Parabéns! Você acertou {acertos} respostas.\nRestam apenas {(len(perguntas) - acertos)}!')
elif acertos == 0:
    print(f'Não desista! Todo mundo começa de algum lugar.\nVocê não acertou nenhuma pergunta... mas eu também já estive em seu lugar.\n\nNão abaixe a cabeça e siga em frente, pois você vai conseguir!')
else:
    print(f'Que pena! Você acertou {acertos} perguntas...\nNão desista! Você precisa acertar mais {len(perguntas) - acertos}.')