
#entrada

altura = float(input("Digite sua altura em metros, (exemplo: 1.70):  "))
sexo = (input("Qual é seu sexo? digite 'm' ou 'f':  "))

#processamento
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
#saida
else:
    peso_ideal = 0
    print("Sexo não reconhecido")
print("Seu peso ideal é {0:.2f}".format(peso_ideal))