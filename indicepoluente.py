#entradas

indice = float(input("Informe o índice de poluição:  "))
#processamento
if indice >=0.3 and indice < 0.4:
    print("Indústrias do 1º Grupo devem suspender as atividades")
elif indice >=0.4 and indice < 0.5:
    print("Indústrias do 1º e 2º Grupos devem suspender as atividades")
elif indice >=0.5: 
    print("Todo o setor industrial deve suspender as atividades")
else:
    print("O setor industrial pode continuar suas atividades normalmente")