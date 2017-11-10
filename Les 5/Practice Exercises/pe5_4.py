hardloper = open('../Files/hardlopers', 'a')

import datetime
vandaag = datetime.datetime.today()
date = vandaag.strftime("%a %d %b %Y, %H:%M:%S")

naam = input('Naam: ')

hardloper.write('{}, {}\n'.format(date, naam))
hardloper.close()



