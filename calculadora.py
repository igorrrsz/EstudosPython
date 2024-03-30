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













