#entradas
valor_por_horas = float(input("qual valor você recebe por hora? "))
horas_trabalhadas = int(input("quantas horas você trabalhou?  "))
#processamento
salario = horas_trabalhadas * valor_por_horas
#saida
print("Nesse mẽs você vai receber R$ {0:.2f}".format(salario))