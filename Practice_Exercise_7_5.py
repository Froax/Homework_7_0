name = True
names = {}
while name:
    newname = input('Volgende naam: ')
    if newname:
        if newname in names:
            names[newname] += 1
        else:
            names[newname] = 1
    else:
        name = False

for i, e in names.items():
    if e == 1:
        print('er is een student met de naam: {0}'.format(i))
    else:
        print('er zijn {0} studenten met de naam: {1}'.format(e, i))