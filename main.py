try:
    n = int(input('Digite um numero: '))
    print(n + 2)
except ValueError:
    print('Valor digitado é inválido')
