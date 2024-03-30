entrada = (input('Você já tem uma conta? S/N: '))
senhaCorreta = 12345
if entrada == 'S' or entrada == 's':
    entrada2 = (input('[E]ntrar [S]air: '))
    if entrada2 == 'E' or entrada2 == 'e':
        senha = int(input('Digite sua senha: '))

        if senha == senhaCorreta:
            print('Bem vindo!')
        else:
            print('Você digitou a senha errada!')
        
    elif entrada2 == 'S' or entrada2 == 's':
        print('Até mais!')

    else:
        print('Você não tomou uma decisão!')

elif entrada == 'N' or entrada == 'n':
    senha = int(input('Digite sua senha: '))
    confSenha = int(input('Confirme sua senha: '))
    if senha == confSenha:
        print('Seu cadastro foi concluído! :) ')

        entrada2 = print(input('[E]ntrar [S]air: '))
        if entrada == 'E' or entrada == 'e':
            senha = int(input('Digite sua senha: '))

            if senha == senhaCorreta:
                print('Bem vindo!')
            else:
                print('Você digitou a senha errada!')
            
        elif entrada == 'S' or entrada == 's':
            print('Até mais!')

        else:
            print('Você não tomou uma decisão!')
    elif senha != confSenha:
        print('As senhas não são iguais')








