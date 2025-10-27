numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: " ))
operador = input("Digite um operador (+ | - | / ): ")

while True:
    if operador == "+":
        soma = numero1 + numero2
        print(soma)

    elif operador == "-":
        sub = numero1 - numero2
        print(sub)

    elif operador == "/":
        div = numero1 / numero2
        print(div)

    else:
        print("Digite um operador!")

    saida = input("Você deseja sair? [s]im: ").lower().startswith('s')
    if saida is True:
        break