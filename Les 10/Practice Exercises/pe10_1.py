import xmltodict

XMLFile = '../Files/XMLArtikelen'

with open(XMLFile, 'r') as file:
    infile = file.read()

XMLDict = xmltodict.parse(infile)

for artikel in XMLDict.get('artikelen').get('artikel'):
    print(artikel.get('naam'))