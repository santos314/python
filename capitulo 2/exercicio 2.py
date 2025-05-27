PrecoCapaLivro = 24.95

PrecoCapaLivroDesconto = PrecoCapaLivro - (PrecoCapaLivro * 0.40)

CustoFretePrimeiroExemplar = PrecoCapaLivro + 3.00

CustoFreteRestanteExemplar = PrecoCapaLivroDesconto + 0.75

CustoTotalAtacado = CustoFretePrimeiroExemplar + (CustoFreteRestanteExemplar * 59)



print ("o preco total de atacado para 60 exemplares é de: ", CustoTotalAtacado)