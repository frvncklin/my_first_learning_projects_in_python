horas = input("Que horas são?\n>>> ")

apenas_hora = horas.isdigit()

if apenas_hora:
    horas = int(horas)
    manha = horas in range(0, 12)
    tarde = horas in range(12, 18)
    noite = horas in range(18, 24)
    if manha:
        print("\nBom dia!")
    elif tarde:
        print("\nBoa tarde")
    elif noite:
        print("\nBoa noite!")
    else:
        print("\nDigite um horário válido! Ex: 0, 3, 15, 18, 23 (entre 0 e 23 horas)")
else:
    print("\nDigite apenas a hora. Ex: 0, 3, 15, 18, 23 (entre 0 e 23 horas)")