# Exibidor de Data de Nacimento com Inputs (básico), uso de argumentos básicos e método 'format'

# Inicializando variáveis de estilo.
arrow = " ---> "
slash = "********"
blank = "        "

# Inicializando o ambiente de entrada de dados.
dia = input("{}  Digite seu dia de Nascimento, mês e ano (completo, ex: 1999)  {}\n{}(Basta ir digitando e pressionando enter para cada um na ordem){}\n{}".format(slash, slash, blank, blank, arrow))
mes = input(arrow)  # Os dados "inputados" sempre seão strings.
ano = input(arrow)

# Output do programa
print("\nDATA DE NASCIMENTO", end= ": ")
print(dia, mes, ano, sep="/", end="\n\n{}{}{}\n".format(slash, slash, slash))
