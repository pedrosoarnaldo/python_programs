lAllPerson = []
lPeso = []
lNome = []

''' Cadastra as pessoas '''
while True:
    lperson = []
    lperson.append(str(input('Nome: ')))
    lperson.append(float(input('Peso: ')))
    lAllPerson.append(lperson[:])
    vContinue = str(input('Continua? [s/n]'))

    if vContinue == 'n':
        break

print(f'Foram cadastras {len(lAllPerson)} pessoas.')


''' Identifica todos os usuários com maior peso'''

for vNome, vPeso in lAllPerson:
    lPeso.append(vPeso)

for vNome, vPeso in lAllPerson:
    if vPeso == max(lPeso):
        lNome.append(vNome)

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

print (f'O menor peso foi de: {min(lPeso)} kg. Peso de: {lNome}')