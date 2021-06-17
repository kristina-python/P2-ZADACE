def ocjena (bodovi):
    if bodovi < 50:
        return "Nedovoljan"
    elif bodovi < 65:
        return "Dovoljan"
    elif bodovi < 80:
        return "Dobar"
    elif bodovi < 90:
        return "Vrlo dobar"
    else:
        return "Odličan"

from csv import reader
datoteka = open("rezultatiispita.csv", "r")

csv_reader = reader(datoteka)

rezultati = list(map(tuple, csv_reader))

novirez = []
for ime, prezime, bodovi in rezultati:
    novirez.append((prezime, ime, bodovi))

novirez.sort()

popis = []

for student in novirez:
    rjecnik = {}
    rjecnik["prezime"] = student[0]
    rjecnik["ime"] = student[1]
    rjecnik["ocjena"] = ocjena(int(student[2]))
    popis.append(rjecnik)

popis2 = []

for student in popis:
    popis2.append((student["prezime"], student["ime"], student["ocjena"]))


print(popis2) 
