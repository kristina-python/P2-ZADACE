#Potrebno napisati regex koji
#vraca podudaranje ukoliko se unese string
#koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
#String mora sadržavati bar jedan broj između 0 i 5 i razmak.
import re

regex = "^k.*[0-5].*\s.*v$"
regex2 = "\s"

while 1:
    unos = input("Unesite ime: ")
    rezultat = re.search(regex and regex2, unos)
    print(rezultat)
    if rezultat:
        break
    else:
        print("Pogrešan unos!") 

print("Ispravan unos") 
