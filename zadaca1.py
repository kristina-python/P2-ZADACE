import random

studenti = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

brojstudenata = {}

ukupno_studenata = len(studenti) 

for student in studenti:
    brojstudenata[student] = 0

for student in studenti:
    if student in brojstudenata:
        brojstudenata[student] += 1
    else:
        brojstudenata[student] = 1


studenti_pojedinacno = []
kljucevi = brojstudenata.keys()
for student in kljucevi:
    studenti_pojedinacno.append(student)

ocjene = {}
pozitivne = 0
jedinice = 0
dvice = 0
trice = 0
cetvrtice = 0
petice = 0

for student in studenti_pojedinacno:
    for i in range(brojstudenata[student]):
        ocjene[student+str(i+1)] = random.randint(1, 5) 
        if ocjene[student+str(i+1)] > 1:
            pozitivne += 1
        if ocjene[student+str(i+1)] == 1:
            jedinice += 1
        elif ocjene[student+str(i+1)] == 2:
            dvice += 1
        elif ocjene[student+str(i+1)] == 3:
            trice += 1
        elif ocjene[student+str(i+1)] == 4:
            cetvrtice += 1
        else:
            petice += 1


parovi = ocjene.items()
for student, ocjena in parovi:
    print(student, "-", ocjena)

print("Prošlo je:", (pozitivne/ukupno_studenata)*100, "%")
print("Jedinice", jedinice)
print("Dvice", dvice)
print("Trice", trice)
print("Cetvrtice", cetvrtice)
print("Petice", petice)



            
            

    
