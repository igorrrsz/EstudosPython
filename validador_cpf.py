# calculo do primeiro dígito do CPF 

entrada = input('Digite seu CPF (Somente números): ')

if len(entrada) != 11:
    print("Erro: Você deve digitar 11 números!")
    exit()

calculo1 = (int(entrada[0]) * 10) + (int(entrada[1]) * 9) + \
           (int(entrada[2]) * 8) + (int(entrada[3]) * 7) + \
           (int(entrada[4]) * 6) + (int(entrada[5]) * 5) + \
           (int(entrada[6]) * 4) + (int(entrada[7]) * 3) + \
           (int(entrada[8]) * 2)

calculo2 = (calculo1 * 10) % 11

primeiro_digito = calculo2 if calculo2 <= 9 else 0 

# calculo do segundo dígito do CPF 

calculo3 = (int(entrada[0]) * 11) + (int(entrada[1]) * 10) + \
           (int(entrada[2]) * 9) + (int(entrada[3]) * 8) + \
           (int(entrada[4]) * 7) + (int(entrada[5]) * 6) + \
           (int(entrada[6]) * 5) + (int(entrada[7]) * 4) + \
           (int(entrada[8]) * 3) + (int(entrada[9]) * 2)

calculo4 = (calculo3 * 10) % 11

segundo_digito = 0 if calculo4 > 9 else calculo4

if int(entrada[9]) == primeiro_digito and int(entrada[10]) == segundo_digito:
    
    print("O CPF é válido!")
    validador = True
else:
    # Código que executa se o CPF for inválido
    print("O CPF é inválido!")
    validador = False

