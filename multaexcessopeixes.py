#entradas
print("O limite de peso é 50kg")
p = float(input("Informe o peso dos peixes: "))

#processamento
if p > 50:
    multa = (p - 50) * 4.00
    e = 'excesso'
    print("Você deverá pagar multa de R${0:.2f}".format(multa))
else:
    multa = 0
    e = 0
    print("Multas : {0}".format(multa))
    print("Excesso: {0}".format(e))
    print("Você não pagará multa")
    
    
    