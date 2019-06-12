time = int( input ('quanto tempo de uso?'))

time_ex = int (time - 10 / (5 * 0.2) )

if time <= 10:
    print("o valor a ser pago é de R$5,00")

elif time > 10:
    print("o valor a ser pago é de:", 5 + time_ex)






