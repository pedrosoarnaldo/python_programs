import random
import math

vChoice = int(input('Escolha um número de 0 até 5: '))
vComputerChoice = int(random.randrange(5))

if vChoice == vComputerChoice:
        print('Você acertou!')
else:
        print('Você errou! o número que o computador escolheu foi {}'.format(vComputerChoice))

if vChoice == 0:
        print('O número que você escolheu não é par nem ímpar é 0')
else:
        vDiv = int(math.floor(vChoice / 2))
        if vDiv == 0:
                print('O número que você escolheu é ímpar')
        else:
                print('O número que você escolheu é par')

vVelocidade = int(input('Qual a velocidade do carro: '))
cMulta = 70.00

if vVelocidade > 80:
        print('Você foi multado e o valor da multa é: {:.2f}'.format((vVelocidade-80) * cMulta))
else:
        print('Tudo certo!')


vKm = int(input('Entre com o km da viagem: '))

print('O Valor a ser pago é {:.2f} R$ 0.50 por km'.format(vKm * 0.50)) if (vKm <= 200) else print('O Valor a ser pago é {:.2f} R$ 0.45 por km'.format(vKm * 0.45))

print('Agora veremos se é possível formar um triangulo a partir do input de 3 valores')

vRetaA = float(input('Tamanho da primeira reta: '))
vRetaB = float(input('Tamanho da segunda reta: '))
vRetaC = float(input('Tamanho da terceira reta: '))

### se tudo for verdadeiro = Triangulo
###| b - c | < a < b + c
###| a - c | < b < a + c
###| a - b | < c < a + b

if (math.fabs(vRetaB - vRetaC) < vRetaA) and (math.fabs(vRetaB - vRetaC) < (vRetaB + vRetaC)):
        if (math.fabs(vRetaA - vRetaC) < vRetaB) and (math.fabs(vRetaA - vRetaC) < (vRetaA + vRetaC)):
                if (math.fabs(vRetaA - vRetaB) < vRetaC) and (math.fabs(vRetaA - vRetaB) < (vRetaA + vRetaB)):
                        print('Pode ser um triângulo')
else:
        print('Os números escolhidos não formam um triângulo')

