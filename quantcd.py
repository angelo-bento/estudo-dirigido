quantCD = int(input("Digite a quantidade de CDs: "))
print("")

a = 0
valorTotal = 0

for x in range(quantCD):
	valorCD = eval(input("Digite o valor do CD: "))
	valorTotal = valorTotal + valorCD
	valorMedio = valorTotal / quantCD
	a = a + 1

print("")
print("O valor total gasto: R$", valorTotal)
print("O valor médio gasto por cada CD foi de: R$", valorMedio)