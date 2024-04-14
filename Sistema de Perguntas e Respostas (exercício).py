def cabecalho(entrada):
    def gerar_cabecalho():
        return f"------------ {entrada.upper()} ------------\n\nautor: daemon.dev\n\n"
    return gerar_cabecalho

cabecalho_programa = cabecalho("sistema de perguntas e respostas - Exercício")

# Isso aqui é uma lista de dicionários.

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print(cabecalho_programa())

exercicios_certos = []
exercicios_errados = []
i = 0

for chave, valor in perguntas[i].items():

    print(f"Exercício {i + 1}: ", end="")
    print(perguntas[i]['Pergunta'])

    print(f"a) {perguntas[i]['Opções'][0]}")
    print(f"b) {perguntas[i]['Opções'][1]}")
    print(f"c) {perguntas[i]['Opções'][2]}")
    print(f"d) {perguntas[i]['Opções'][3]}")

    escolha_usuario = input("\n>>> ").lower()

    if i == 0:
        if escolha_usuario.startswith("c"):
            exercicios_certos.append(f"{i + 1}")
        else:
            exercicios_errados.append(f"{i + 1}")
            
    elif i == 1:
        if escolha_usuario.startswith("a"):
            exercicios_certos.append(f"{i + 1}")
        else:
            exercicios_errados.append(f"{i + 1}")
        
    elif i == 2:
        if escolha_usuario.startswith("b"):
            exercicios_certos.append(f"{i + 1}")
        else:
            exercicios_errados.append(f"{i + 1}")
        

    print('')

    if i == 2:
        break

    i += 1

print("-----------------------------------------\n")
if len(exercicios_certos) > len(exercicios_errados):
    print("Parabéns!")
elif len(exercicios_errados) > len(exercicios_certos):
    print("Que pena!")

if len(exercicios_certos) <= 2:
    print(f"\nVocê acertou {len(exercicios_certos)} questões.")
    print(f"--> Atenção com os exercícios: {exercicios_errados}!")
elif len(exercicios_certos) == 3:
    print(f"\nVocê acertou todas as questões!")

print("\n-----------------------------------------")
