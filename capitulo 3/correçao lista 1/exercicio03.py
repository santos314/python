def calculoDiametro(raio):
   return 2 * raio

def calculoCircunferencia(PI, raio):
   return 2 * PI * raio

def calculoArea(PI, raio):
   return PI * (raio ** 2)

#main
raio = float(input("digite o raio do circulo: "))
PI = 3.14159

diametro = calculoDiametro(raio)
circunferencia = calculoCircunferencia(PI, raio)
area = calculoArea(PI, raio)

print("Diâmetro: ", diametro)
print("Circunferência: ", circunferencia)
print("Área: ", area)

#diametro = 2 * raio circunferencia = 2 * PI * raio area = PI * (raio **2)
