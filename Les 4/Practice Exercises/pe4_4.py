oudwachtwoord = input('Oude wachtwoord: ')
nieuwwachtwoord = input('Nieuwe wachtwoord: ')

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) > 6:
        resultaat = True
    else:
        resultaat = False
    return resultaat

print(new_password(oudwachtwoord, nieuwwachtwoord))
