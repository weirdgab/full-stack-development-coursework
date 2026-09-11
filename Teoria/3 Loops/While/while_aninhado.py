while True:
    print('Você está no primeiro laço.')
    opcao1 = input("Deseja sair dele? Digite 'SIM' para isso: \n")
    if opcao1 == 'SIM':
        break
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input("Deseja sair dele? Digite 'SIM' para isso: \n")
            if opcao2 == 'SIM':
                break
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço.')
