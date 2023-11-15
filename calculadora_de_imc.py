# Inicializando estilização.

arrow = "-----#"
blank_space = 15 * (" ")
author_name = "souto_frvncklin"
mensagem_final = "Obrigado por usar o programa!"

# Printando cabeçalho.

print("{}CALCULADORA DE I.M.C.\n{}{}autor: {}\n".format(blank_space, blank_space, blank_space, author_name))

# Inicializando e obtendo do usuário as variáveis dos dados da ficha.

nome = input("Insira seu nome:\n>>> ")
altura = int(input("Sua altura (em centímetros):\n>>> "))
peso = int(input("Por fim, seu peso (em kg):\n>>> "))

# Calculando IMC.

imc = peso / ((altura * altura) / 10000) 

# Printando o output dos dados.

print("\n{} FICHA DE CADASTRO:\n\nNome: {}\nAltura: {} cm\nPeso: {} kg\nIMC: {:.1f}".format(arrow, nome, altura, peso, imc))

# Realizando branches de diagnóstico, de acordo com o valor do I.M.C.

if imc < 18.5:
    print("DIAGNÓSTICO: Magreza.")
elif 18.5 <= imc <= 24.9:
    print("DIAGNÓSTICO: Normal")
elif 25 <= imc <= 29.9:
    print("DIAGNÓSTICO: Sobrepeso")
elif 30 <= imc <= 34.9:
    print("DIAGNÓSTICO: Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("DIAGNÓSTICO: Obesidade grau II")
elif imc >= 40:
    print ("DIAGNÓSTICO: Obesidade grau III")

# Mensagem final: 

print("\n{}{}".format(blank_space, mensagem_final))
print("Fontes: https://www.tuasaude.com/calculadora/imc/")

