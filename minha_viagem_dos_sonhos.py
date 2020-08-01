passagem = 1500

print(passagem)

custo_por_dia = 350

dias = 2

custo_total = passagem * 2 + custo_por_dia * dias

print(custo_total)

print ("O custo de sua passagem será: R$ 3700,00. ")

print ("O custo de sua passagem será: R$", custo_total)

dólar = 5.01

print("O custo de sua passagem será: US$", custo_total/dólar)

print("Qual é o nome do senhor?")

nome = input()

print(nome,"," "o custo total de sua passagem é de:", custo_total)

print("O senhor vai querer parcelar?")

parcelar = input()

print("Podemos parcelar até em 6 vezes!")

print("Ok, por favor, pode parcelar em 6 vezes então!", "Obrigado.")

print(nome, "o preço de sua passagem parcelada será de:")

preço_parcela = float(input())

print("Muito obrigado, Sr.", nome, "por escolher a Viaje Comigo como agência de sua viagem," "o preço da parcela ficará em 6x de", preço_parcela, "pagos em cartão de crédito.")

print(nome, "Podemos fechar o contrato?")

contrato = input()

print("Perfeito, mais uma vez muito obrigado pela preferência, Sr", nome, ".", "Tenha um ótimo e excelente dia.")