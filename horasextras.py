#constantes
valor_hora = 10.00
valor_hora_extra = 20.00
#variaveis
e = 0
#entradas
c = int(input("Informe o código:  "))
n = float(input("Informe a quantidade de horas trabalhadas: "))

#processamento
if n > 50:
    e = (n - 50) * valor_hora_extra
    salario = (50 * valor_hora) + e
    print("Salário Total R$ {0:.2f}".format(salario))
    print("Salário Excedente R$ {0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("Salário Total R$ {0:.2f}".format(salario))
    print("Salário excedente R$ {0:.2f}".format(e))
    