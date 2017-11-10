def index(textfile, list):
    try:
        infile = open(textfile)
        lines = infile.readlines()
        infile.close()

        print('{} and {}'.format(lines, list))
    except IOError:
        print('File {} not found'.format(textfile))

index('../Files/raven.txt', ['hello', 'goodbye'])
