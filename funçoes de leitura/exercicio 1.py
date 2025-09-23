def apresentacao(nome, nomePai, nomeMae):
    print(f"Nome:  {nome}")
    print(f"Nome do pai:  {nomePai}")
    print(f"Nome da mae:  {nomeMae}")


nome = str(input("digite seu nome"))
nomePai = str(input("digite o nome da sua mae"))
nomeMae = str(input("digite o nome do seu pai"))

apresentacao(nome,nomePai,nomeMae)
