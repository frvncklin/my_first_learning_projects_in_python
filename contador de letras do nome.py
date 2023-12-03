nome = input("Digite seu primeiro nome: ")

nome_curto = len(nome)  in range(0, 5)
nome_normal = len(nome) in range(5, 7)

if nome_curto:
    print("\nSeu nome é curto!")
elif nome_normal:
    print("\nSeu nome é normal.")
else:
    print("\nUau! Seu nome é muito grande!")