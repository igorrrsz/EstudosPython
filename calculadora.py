# Calculadora básica: Solicite ao usuário um número, um operador e em seguida outro
# número, por exemplo: 1 + 1 2.3 * 2 5 – 2.7 9.3 / 2.4
# • Interprete a expressão e dê o resultado correto;
# • Cada operação matemática deve ser uma função que retorna o resultado da 
# operação para o chamador;
# • A impressão do resultado deve ser feita a partir do chamador

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
    
def multiplicacao(a, b):
    return a * b
    
def divisao(a, b):
    return a / b

entrada = (input('Digite a operação matemática: '))

calculo = entrada.split()
operador = calculo[1]
a = float(calculo[0])
b = float(calculo[2])

if operador == '+':
    resultado = soma(a, b)
    
elif operador == '-':
    resultado = subtracao(a, b)
    
elif operador == '*':
    resultado = multiplicacao(a, b)
    
elif operador == '/':
    resultado = divisao(a, b)

else:
    print('Digite um número!')
    
print(resultado)













