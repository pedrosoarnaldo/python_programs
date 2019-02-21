listTotal = [[],[]]
valor = 0

for i in range(0,7):
    valor = int(input('Entre com o valor: '))

    if (valor % 2) == 0:
        listTotal[0].append(valor)
    else:
        listTotal[1].append(valor)

print('--*--' *15)
print('Pares: ', end='')
print(sorted(listTotal[0]))
print('--*--' *15)
print('Impares: ', end='')
print(sorted(listTotal[1]))
print('--*--' *30)