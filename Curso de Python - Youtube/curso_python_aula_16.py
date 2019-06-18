import random

vNumber = 10

tNumber = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while (vNumber < 0) or (vNumber > 5):
    vNumber = int(input('Entre com o número entre 0 e 5: '))

print('Você digirou o número: {}'.format(tNumber[vNumber]))


tTeams = ('São Paulo', 'Vasco', 'Corinthians', 'Palmeiras', 'Santos', 'Sport', 'Bahia')

print('Os cinco primeiros são: {}'.format(tTeams[0:5]))
print('Os quatro últimos são: {}'.format(tTeams[-4:]))
print('Times em ordem alfabética: {}'.format(sorted(tTeams)))

print('O São Paulo está em: {}'.format(tTeams.index('São Paulo')+1))

del(tNumber)


tNumber = (random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99), random.randint(0,99))

print('todos os números sorteados: {}'.format(tNumber))
print('O maior número é: {}'.format(max(tNumber)))
print('O menor número é: {}'.format(min(tNumber)))

del(tTeams)

