passagem = 1500

custo_por_dia = 350

dias = 14

custo_total = passagem * 2 + custo_por_dia * dias

print("O custo de sua viagem será: R$", custo_total)

parcelas = int(input())

valor_das_parcelas = custo_total/parcelas

print("Usando parcelamento, você selecionou parcelas em", parcelas, "x sem juros. O valor de cada parcela será: R$", valor_das_parcelas)