def monopolyworp():
    dobbel1 = random.randrange(1, 7)
    dobbel2 = random.randrange(1, 7)
    aantalkeerachterelkaar = 0
    nogdoorgaan = True

    while nogdoorgaan:
        dobbel1 = random.randrange(1, 7)
        dobbel2 = random.randrange(1, 7)

        if dobbel1 == dobbel2 and aantalkeerachterelkaar == 3:
            print('{} + {} = {} (direct naar de gevangenis)'.format(dobbel1, dobbel2, dobbel1 + dobbel2))
            nogdoorgaan = False
        elif dobbel1 == dobbel2:
            print('{} + {} = {} (dubbel)'.format(dobbel1, dobbel2, dobbel1 + dobbel2))
            aantalkeerachterelkaar += 1
        else:
            print('{} + {} = {}'.format(dobbel1, dobbel2, dobbel1 + dobbel2))
            nogdoorgaan = False

import random

monopolyworp()