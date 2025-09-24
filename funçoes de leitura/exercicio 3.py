def soma(n1, n2):
    operacão = n1 + n2
    print(f"o resultado da soma é: ", operacão)

def subtracão(n1, n2):
    operacão = n1 - n2
    print(f"o resultado da subtracão é: ", operacão)

def multiplicacão(n1, n2):
    operacão = n1 * n2
    print(f"o resultado da multiplicacão é: ", operacão)

def divisão(n1, n2):
    operacão = n1 / n2
    print(f"o resultado da divisão é: ", operacão)



n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))

soma(n1, n2)
subtracão(n1, n2)
multiplicacão(n1, n2)
divisão(n1, n2)