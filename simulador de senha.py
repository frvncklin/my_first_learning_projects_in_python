senha_salva = '123456'
senha_digitada = ''
repeticoes = 0
proibicao = False

print('Bem vindo á HOSEON TECH!\n')
print("Digite sua senha por favor: ")

while senha_digitada != senha_salva:
    senha_digitada = input(">>> ")
    repeticoes += 1

    if repeticoes % 3 == 0:         # Esse código faz a dica da senha aparecer a cada 3 tentativas
        print("Dica da senha: Sequencia de números conhecida. Possui 6 dígitos.\n")
    elif repeticoes >= 16:          # Esse código quebra o loop caso as tentativas excedam o limite e informa que o sistema foi bloqueado.
        print("------------- SISTEMA BLOQUEADO -------------\n            Contate o administrador          \n\nDiagnóstico: Excesso de repetições.")
        proibicao = True
        break

if proibicao == False:   # Ao acertar a senha, essa mensagem aparecerá.
    print('\n-------------- SISTEMA ONLINE ----------------')
    print(f"\nTotal de {repeticoes} tentativas de senha.")
else:
    print("Fim do sistema.")
