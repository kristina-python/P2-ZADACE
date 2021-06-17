def parni_brojevi(n):
    for i in range(n):
        if i%2==0:
            yield i
            
def neparni_brojevi(n):
    for i in range(n):
        if i%2==0:
            yield i

broj = int(input("Unesite neki broj: "))
generator_parnih = parni_brojevi(broj)
generator_neparnih = neparni_brojevi(broj)

brojevi = zip(generator_parnih, generator_neparnih)

print("Parni:            Neparni:")

for parni, neparni in brojevi:
    print(" ", parni, " ", neparni) 
