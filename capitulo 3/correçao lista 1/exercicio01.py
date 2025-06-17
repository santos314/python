def adicao(numero1, numero2):
   return numero1 + numero2

def subtracao(numero1, numero2):
   return numero1 - numero2

def multiplicacao(numero1, numero2):
   return numero1 * numero2

   def divisao(numero1, numero2):
       return numero1 / numero2

# main
numero1 = int(input("digite o primeiro número "))
numero2 = int(input("digite o primeiro número "))

resultadoAdicao = adicao(numero1, numero2)
resultadoSubtracao = subtracao(numero1, numero2)
resultadoMultiplicacao = multiplicacao(numero1, numero2)
resultadoDivisao = divisao(numero1, numero2)

print("Adição: ", resultadoAdicao)
print("Subtração: ", resultadoSubtracao)
print("Multiplicação: ", resultadoMultiplicacao)
print("divisão: ", resultadoDivisao)