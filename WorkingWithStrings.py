vString = str(input('Entre com seu nome completo: '))

### Apresentar tudo como maiusculo
print(vString.upper())

### Apresentar tudo em minusculo
print(vString.lower())

### Quantas letras ao todo sem considerar espaço
vCount = len(vString) - vString.count(' ')
print('Quantidade de letras = {}'.format(vCount))

### quantas letras tem o primeiro nome
vSplit = vString.split()
print('Quantidade de letras do Primeiro Nome: {}'.format(len(vSplit[0])))

### Verifica se o nome começa com Santo
if vString[0:5].find('Santo') >= 0:
    print('Seu nome começa com Santo')
else:
    print('Seu nome não começa com Santo')

### Verifica se o nome tem SILVA
if vString.upper().find('SILVA') < 0:
    print('Você não tem Silva no nome')
else:
    print('Você tem Silva no nome')

### Imprime o primeiro nome
print('Primeiro Nome: {}'.format(vString.split()[0]))

### Imprime o último nome
print('Último Nome: {} '.format(vString.split()[-1]))

### Recebe numero e divide em
###
### Unidade
### Centena
### Dezena
### Milhar

vNum = input('Entre com um número de 0 até 9999: ')

if int(vNum) < 0 :
        print('Número deve ser maior que 0')
        exit(1)

if int(vNum) > 9999 :
        print('Número deve ser menor que 9999')
        exit(1)

vLNum = vNum.rjust(4).replace(' ','0')

print('Unidade: {}'.format(vLNum[3]))
print('Dezena: {}'.format(vLNum[2]))
print('Centena {}'.format(vLNum[1]))
print('Milhar {}'.format(vLNum[0]))

### Receber uma string e dizer
### Quantas vezes aparece a letra A
### Em que posição ela aparece pela primeira vez
### Em que posição ela aparece pala última vez

vString = str(input('Entre com uma String: '))

vPosicaoInicial = vString.upper().find('A')
vCount = vString.upper().count('A')
vPosicaoFinal = len(vString) - (vString[::-1]).upper().find('A') - 1

if vCount == 0:
    vCount = 0
    vPosicaoInicial = 0
    vPosicaoFinal = 0

print('A letra "A" aparece {} vezes'.format(vCount))
print('A letra "A" aparece pela primeira vez na posição {}'.format(vPosicaoInicial))
print('A letra "A" aparece pela última vez na posição {}'.format(vPosicaoFinal))
