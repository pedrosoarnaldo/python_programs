lAllPerson = []
lPeso = []
lNome = []
lperson = []

''' Cadastra as pessoas '''
while True:
    ''' lperson = [] pode ser substituido pela linha lperson.clear()'''
    lperson.append(str(input('Nome: ')))
    lperson.append(float(input('Peso: ')))
    lAllPerson.append(lperson[:])
    lperson.clear()

    vContinue = str(input('Continua? [s/n]'))
    if vContinue in 'Nn':
        break

print('-=' *30)
print(f'Foram cadastras {len(lAllPerson)} pessoas.')


''' Identifica todos os usuários com maior peso'''

for vNome, vPeso in lAllPerson:
    lPeso.append(vPeso)

for vNome, vPeso in lAllPerson:
    if vPeso == max(lPeso):
        lNome.append(vNome)

print('-=' *30)
print (f'O maior peso foi de: {max(lPeso)} kg. Peso de: {lNome}')

''' Zera as listas intermediárias '''
lPeso = []
lNome = []

''' Identifica todos os usuários com menor peso'''

for vNome, vPeso in lAllPerson:
    lPeso.append(vPeso)

for vNome, vPeso in lAllPerson:
    if vPeso == min(lPeso):
        lNome.append(vNome)

print('-=' *30)
print (f'O menor peso foi de: {min(lPeso)} kg. Peso de: {lNome}')

print('-=' *30)