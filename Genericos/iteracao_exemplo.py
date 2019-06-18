import time

for i in range(1,11):
    print('{}'.format(11-i))
    time.sleep(1)

print('Feliz Ano Novo!!!')

i = 10
while i >= 1:
    print('{}'.format(i))
    time.sleep(1)
    i = i - 1

print('Feliz Ano Novo!!!')

x = 0

''' comentario '''

while x != 9:
    print('Dentro do Loop')
    x = int(input('Entre com número: '))
    if x == 9:
        break

print('Fora do loop')
