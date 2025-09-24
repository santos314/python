def resultadoTabuada(numero, tabuada):
    while tabuada <= 10:
        print(f"a tabuada do seu numero é:", numero * tabuada)
        tabuada += 1

numero = int(input("Digite um número inteiro: "))
tabuada = 1
resultadoTabuada(numero, tabuada)