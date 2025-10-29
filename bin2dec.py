entradaBinarios = input("Digite um número binário (somente 0s e 1s, até 8 dígitos): ")

if len(entradaBinarios) > 8:
    print("O número deve ter no máximo 8 dígitos!")
elif '0' not in entradaBinarios and '1' not in entradaBinarios:
    print("Você precisa digitar pelo menos um 0 ou 1!")
elif any(c not in '01' for c in entradaBinarios):
    print("Você não pode inserir outro número que não seja 0 ou 1!")
else:
    entradaInt = int(entradaBinarios, 2)
    print(f"O valor decimal é: {entradaInt}")