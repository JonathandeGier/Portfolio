lengte = int(input('Lengte in cm: '))

def lang_genoeg(cm):
    if cm >= 120:
        resultaat = 'Je bent lang genoeg voor de attractie!'
    else:
        resultaat = 'Sorry, je bent te klein!'
    return resultaat

print(lang_genoeg(lengte))
