def right_justify(palavra, tamanhoPalavra):
    espaco = " " * (70-tamanhoPalavra)
    return espaco + palavra


#main
palavra = str(input("digite uma palavra: "))
tamanhoPalavra = len(palavra)
espacamentoPalavra = right_justify(palavra, tamanhoPalavra)

print(espacamentoPalavra)