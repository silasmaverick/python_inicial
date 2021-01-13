#entrada
idade = int(input("Informe a idade do nadador"))

#processamento
if idade >=4 and idade <=7:
    print("O nadador pertence ao grupo Infantil A")
elif idade >= 8 and idade <= 11:
    print(" O nadador pertence ao grupo Infantil B")
elif idade >= 12 and idade <= 14:
    print("O nadador pertence ao grupo Juvenil A")
elif idade >= 15 and idade <= 17:
    print("O nadador pertence ao grupo Juvenil B")
elif idade >= 18:
    print("O nadador pertence ao grupo Adulto")
else:
    print("Pessoa sem idade mínima")