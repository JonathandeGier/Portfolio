def week():
    doorgaan = True
    while doorgaan:
        afkorting = input('Typ afkorting van dag (met hoofdletter): ')

        if afkorting == 'Ma':
            dag = 'Maandag'
        elif afkorting == 'Di':
            dag = 'Dinsdag'
        elif afkorting == 'Wo':
            dag = 'Woensdag'
        elif afkorting == 'Do':
            dag = 'Donderdag'
        elif afkorting == 'Vr':
            dag = 'Vrijdag'
        elif afkorting == 'Za':
            dag = 'Zaterdag'
        elif afkorting == 'Zo':
            dag = 'Zondag'
        elif afkorting == '':
            doorgaan = False
            dag = ''
        else:
            dag = 'Unknown'
        print(dag)

week()
