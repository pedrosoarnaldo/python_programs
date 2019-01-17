import datetime

vCasa = float(input('Qual o valor do financiamento: '))
vAnos = int(input('Em quantos anos pretende pagar: '))
vSalario = int(input('Qual a sua renda mensal: '))
vPrestacoes = int(vAnos * 12)
vValorMensal = float(vCasa / vPrestacoes)

print('O valor da prestação será: {:.2f} e você pagará em {} prestações.'.format(vValorMensal,vPrestacoes))

if vValorMensal > (vSalario - (vSalario * 0.3)):
    print('Infelizmente o valor de prestação é maior do que 30% do seu salário!')
    exit(1)

print('')
vNumero = int(input('Entre com um número qualquer: '))
vConversao = str(input('Qual a base de conversão [binario, octal, hexadecimal]? '))

if vConversao == 'binario':
    print('{0:d} em binário é: {0:#b}'.format(vNumero))
elif vConversao == 'octal':
    print('{0:d} em octal é: {0:#o}'.format(vNumero))
else:
    print('{0:d} em hexadecimal é: {0:#x}'.format(vNumero))

print('')
vNumero1 = int(input('Entre com outro número: '))

if vNumero > vNumero1:
    print('O número {} é maior que o número {}'.format(vNumero, vNumero1))
elif vNumero < vNumero1:
    print('O número {} é menor que o numero {}'.format(vNumero, vNumero1))
else:
    print('Os números são iguais')

print('')
vAnoNascimento = int(input('Entre com seu ano de nascimento: '))

### yyyy-mm-dd
vDate = str(datetime.date.today())

vString = vDate.split('-')
vAno = int(vString[0]) - vAnoNascimento

if vAno >= 17 and vAno <=18:
    print('Está na hora de se alistar')
elif vAno < 17:
    print('Ainda faltam {} anos para o alistamento'.format(18-vAno))
else:
    print('Já se passaram {} anos dese o seu ano limite para o alistamento'.format(vAno-18))

