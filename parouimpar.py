#variaveis
p = 0
i = 0
#entrada
numero = int(input("digite um número: "))

#processamento
if numero % 2 == 0:
    p = numero
    print ("{0} é um numero par".format(p))
else:
    i = numero
    print ("{0} é um número impar".format(i))

print (p)
print (i)