studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for student in studentencijfers:
        antw = antw + [round(sum(student) / len(student))]
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddeldelijst = gemiddelde_per_student(studentencijfers)
    
    antw = round(sum(gemiddeldelijst) / len(gemiddeldelijst))
    return antw


print('Gemiddelde per student: {}'.format(gemiddelde_per_student(studentencijfers)))
print('Gemiddelde van alle studenten: {}'.format(gemiddelde_van_alle_studenten(studentencijfers)))