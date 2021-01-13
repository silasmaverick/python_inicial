#variaveis
contador_total = 0
cont_situacao_1 = 0 #necessita de esfara nova
cont_situacao_2 = 0 #necessita de limpeza
cont_situacao_3 = 0 #necessita de trocar o cabo
cont_situacao_4 = 0 #Inutilizavel
# entrada/processamento
patrimonio = int(input("Digite o patrimônio do mouse"))
print("Os seguintes defeitos estão indentificados por números")
print("1 - necessita de esfera nova")
print("2 - necessita de limpeza")
print("3 - necessita de trocar o cabo")
print("4 - Inutilizavel")
while patrimonio !=0:
    
    defeito = int(input("Informe o número do defeito: "))
#processamento
    if defeito == 1:
        cont_situacao_1 = cont_situacao_1 + 1
        print("Salvo")
        patrimonio = int(input("Digite o patrimônio do mouse"))
        
    elif defeito ==2:
        cont_situacao_2 = cont_situacao_2 + 1
        print("Salvo")
        patrimonio = int(input("Digite o patrimônio do mouse"))
        
    elif defeito ==3:
        cont_situacao_3 = cont_situacao_3 + 1
        print("Salvo")
        patrimonio = int(input("Digite o patrimônio do mouse"))
        
    elif defeito ==4: 
        cont_situacao_4 = cont_situacao_4 + 1
        print("Salvo")
        patrimonio = int(input("Digite o patrimônio do mouse"))
        
    else:
        print("Infome um número válido")
        
    contador_total = contador_total + 1
p1 = cont_situacao_1 / contador_total *100
p2 = cont_situacao_2 / contador_total *100
p3 = cont_situacao_3 / contador_total *100
p4 = cont_situacao_4 / contador_total *100

#saída

print("Situação                          Quantidade               Percentual")
print(" 1- Necessita de esfera nova            {0}                     {1:.2f}".format(cont_situacao_1,p1))
print(" 2- Necessita de limpeza                {0}                     {1:.2f}".format(cont_situacao_2,p2))
print(" 3- Necessita de trocar o cabo          {0}                     {1:.2f}".format(cont_situacao_3,p3))
print(" 4- inutilizável                        {0}                     {1:.2f}".format(cont_situacao_4,p4))

