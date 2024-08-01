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

def check_response(user_response):
    while True:
        if user_response in possible_options[0 : len(pergunta['Opções'])] and len(user_response) == 1:
            return user_response

        user_response = input('Incorrect option, type a valid one: ')

def validate_response(user_response):
    user_response = pergunta['Opções'][possible_options.index(user_response)]
    return user_response

import os, time

correct_answers = 0
possible_options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

for pergunta in perguntas:

    for chave, valor in pergunta.items():

        if chave == 'Opções':   # Printing options.
            for i, opcao in enumerate(pergunta['Opções']):
                print(f'{possible_options[i]}) {opcao}')
            continue

        elif chave == 'Resposta': # Recieving answer from user.
            resposta_user = input('\nDigite sua resposta: ')
            resposta_user = check_response(resposta_user)    # Checking if the user's answer is a valid one.
            resposta_user = validate_response(resposta_user) # Converting the user's answer in it's valid equivalent in the options list, to be compared to the correct answer accordingly.
            
            resposta_correta = pergunta['Resposta'] 
    
            if resposta_user == resposta_correta:   # Checking if the user response is the right one.
                print()
                print("---> Correto!")
                correct_answers += 1
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
if correct_answers == len(perguntas):
    print('Parabéns! Você acertou todas as perguntas!')
elif len(perguntas) / 2 <= correct_answers < len(perguntas):
    print(f'Parabéns! Você acertou {correct_answers} respostas.\nRestam apenas {(len(perguntas) - correct_answers)}!')
elif correct_answers == 0:
    print(f'Não desista! Todo mundo começa de algum lugar.\nVocê não acertou nenhuma pergunta... mas eu também já estive em seu lugar.\n\nNão abaixe a cabeça e siga em frente, pois você vai conseguir!')
else:
    print(f'Que pena! Você acertou {correct_answers} perguntas...\nNão desista! Você precisa acertar mais {len(perguntas) - correct_answers}.')

# Essa solução é escalável. Se você quiser fazer isso com o seu questionário.
# This solution is scalable. If you may wish, you can do it with your own questionary.

# by kvtana
