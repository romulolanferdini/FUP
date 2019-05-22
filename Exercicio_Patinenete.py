tempo = int (input ("Quanto tempo você utilizou o patinente em minutos? "))

tempo_ex = int (tempo - 10 / (5 * 0.2))

if tempo <= 10:
    print ("O valor a ser pago é de R$ 5,00")

elif tempo > 10:
    print ("O valor é de R$: ", 5 + tempo_ex)

