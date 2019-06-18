def getaction():
    laction = []
    while True:
        laction.append(str(input('Action (Boost|Dodge|Focus|Roll|Target): ')))
        vbreak = input(str('Is it the end of actions (s/n) ? '))
        print('')
        if vbreak == 's' or vbreak == 'S':
            break
    return laction


def getimprovement():
    limprovement = []
    while True:
        limprovement.append(str(input('Improvement (Elit Pilot|Torpedos|Astromech): ')))
        vbreak = input(str('Is it the end of improvements (s/n) ? '))
        print('')
        if vbreak == 's' or vbreak == 'S':
            break
    return limprovement


def getpilot():
    vname = str(input('Name: '))
    vskillpoint = int(input('Skill: '))
    vattackdice = int(input('Attack: '))
    vdefensedice = int(input('Defense: '))
    vhull = int(input('Hull: '))
    vshield = int(input('Shield: '))
    laction = getaction()
    limprovement = getimprovement()
    vtotalpoints = int(input('Total points: '))
    dpilot = {'name': vname, 'skill': vskillpoint, 'attack': vattackdice, 'defense': vdefensedice, 'hull': vhull,
              'shield': vshield, 'action': laction, 'improvement': limprovement, 'points': vtotalpoints}
    return dpilot

def getsquadron(vclass):
    lsquadron = []
    while True:
        lsquadron.append(getpilot())
        vbreak = input(str('Is it the end of pilots (s/n) ? '))
        print('')
        if vbreak == 's' or vbreak == 'S':
            break
    return lsquadron


lsquad1 = getsquadron('Rebel')
lsquad2 = getsquadron('Imperial')

print(lsquad1)
print(lsquad2)