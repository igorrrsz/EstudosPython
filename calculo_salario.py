import os 

def salariobruto(valorhora, horastrabalhadas):
    return valorhora * horastrabalhadas
    
def valorinss(salariobruto):
    return salariobruto * 0.11

def valorsindicato(salariobruto):
    return salariobruto * 0.2

def salarioliquido(salariobruto, descontosindicato, descontovalorinss):
    return salariobruto - descontosindicato - descontovalorinss
def limpartela():
    # Para sistemas Unix/Linux
    if os.name == 'posix':
        _ = os.system('clear')
    # Para sistemas Windows
    elif os.name == 'nt':
        _ = os.system('cls')
        
#programa principal

entradavalorhora = float(input('Quanto você ganha por hora?: '))
entradavalorhoratrabalhada = float(input('Quantas horas você trabalhou este mês?: '))

if entradavalorhora and entradavalorhora:
    
    salario_bruto = salariobruto(entradavalorhora, entradavalorhoratrabalhada)
    valor_inss = valorinss(salario_bruto)
    valor_sindicato = valorsindicato(salario_bruto)
    salario_liquido = salarioliquido(salario_bruto, valor_sindicato, valor_inss)
    
    
    while True:
        print('MENU')
        print('1. Ver o salário bruto.')
        print('2. Ver quanto pagou ao INSS.')
        print('3. Ver quanto pagou ao sindicato.')
        print('4. Ver salário líquido.')
        print('5. Sair.')
        opcao = input('Qual opção você deseja?: ')  
        limpartela()
        if opcao == '1':
            print(f'Salário bruto: R$ {salario_bruto:.2f}')
            
        elif opcao == '2':
            print(f'Desconto do INSS R$ {valor_inss:.2f}')
            
        elif opcao == '3':
            print(f'Desconto do Sindicato: R$ {valor_sindicato:.2f}')
            
        elif opcao == '4':
            print(f'Salário Líquido: R$ {salario_liquido:.2f}')
            
        elif opcao == '5':
            print('Volte sempre!')
            break
        
        else:
            print('Digite uma opção!')
        limpartela()