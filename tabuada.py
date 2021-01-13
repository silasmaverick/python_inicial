#entrada
numero = int(input("Informe um número:  "))
while numero < 1 or numero > 10:
    numero = int(input("Informe um número entre 1 e 10:  "))
print("Tabuada do {0}".format(numero))
for n in range (1,21):
    print("{0} x {1} = {2} ".format(numero, n, (numero * n)))