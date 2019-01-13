import math
import emoji

vNumber = float(input('Please give me a float number:'))
print(math.trunc(vNumber))
print(emoji.emojize('Python is :thumbs_up:'))

# a2 = b2 + c2

vB = float(input('Entre com o cateto 1: '))
vC = float(input('Entre com o cateto 2: '))

print('O Valor da hipotenusa é: ', math.hypot(vB, vC))

vAngulo = float(input('Entre com o ângulo: '))

vSeno = math.sin(math.radians(vAngulo))
vCosseno = math.cos(math.radians(vAngulo))
vTangente = math.tan(math.radians(vAngulo))

print('O ângulo {} tem o Seno = {:.2f}, o Cosseno = {:.2f} e a Tangente = {:.2f}'.format(vAngulo, vSeno, vCosseno, vTangente))
