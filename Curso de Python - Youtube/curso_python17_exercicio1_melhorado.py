lAllPerson = []
lPeso = []
lNome = []
lPerson = []

''' Cadastra as pessoas '''
while True:
    lPerson.append(str(input('Nome: ')))
    lPerson.append(float(input('Peso: ')))

    if len(lAllPerson) == 0:
        vMinPeso = vMaxPeso = lPerson[1]

    if lPerson[1] > vMaxPeso:
        vMaxPeso = lPerson[1]
    else:
        if lPerson[1] <= vMinPeso:
            vMinPeso = lPerson[1]

    lAllPerson.append(lPerson[:])
    lPerson.clear()

    vContinue = str(input('Continua? [s/n]'))
    if vContinue in 'Nn':
        break

print('-=' *30)
print(f'Foram cadastras {len(lAllPerson)} pessoas.')
print('-=' *30)
print(f'O menor peso cadastrado foi: {vMinPeso}.', end='')

for p in lAllPerson:
    if p[1] == vMinPeso:
        print(f' [{p[0]}]',end='')A

print('')
print('-=' *30)
print(f'O maior peso cadastrado foi: {vMaxPeso}.', end='')

for p in lAllPerson:
    if p[1] == vMaxPeso:
        print(f' [{p[0]}]',end='')

print('')
print('-=' *30)