from random import randrange

sucet = 0
while sucet < 21:
    print('Máš', sucet, 'bodov')
    odpoved = input('Otočit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otočil/a si', karta)
        sucet = sucet + karta
    elif odpoved == 'nie':
        break
    else:
        print('Nerozumiem! Odpovedaj "ano", alebo "nie"')

if sucet == 21:
    print('Gratulujem! Vyhrál/a si!')
elif sucet > 21:
    print('Bohuzial!', sucet, 'bodov je vela!')
else:
    print('Chybal len', 21 - sucet, 'bodov!')
