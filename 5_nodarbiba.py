# Uzdevums: Uzrakstat for ciklu, kas izvada skaitļus 
# no 0 līdz 10 izlaižot skaitļus 4 un 6
for iii in range(0, 11):
    if iii != 4 or iii != 6:
        print(iii)
# Uzdevums uzrakstat šo for ciklu kā while ciklu
skaitītājs = 0
while skaitītājs < 11:
    if iii != 4 or iii != 6:
        print(skaitītājs)
    skaitītājs += 1 # palielina skaitītājs par 1

# Uzdevums: Ir dots saraksts
saraksts = [ 0, 5, 4, 9, 10, 12 ]
# Neizmantojot funkciju sum, uzrakstat ciklu, kas saskaita
# visas vērtības šajā sarakstā un izvada rezultātu.
rezultāts = 0
for vērtība in saraksts:
    rezultāts += vērtība
print(rezultāts)

# Uzdevums: aprēķini faktoriāli lietotāja ievadītajam skaitlim
# Faktoriālis - skaitlis kas veidojas reizinot visus skaitļus no
# 1 līdz n., t.i. 3! == 1*2*3.
# Uzrakstat programmu kas veic šo aprēķinu.
ievade = int(input("Ievade: "))
rezultāts = 1
for iii in range(1, ievade + 1):
    rezultāts *= iii
print(rezultāts)

# Iesniegšana e-klasē - pie atbildes iesniegšanas (šī stunda)
# Obligāta prasība - failam ir pareizs paplašinājums (.py)

# Jāuzraksta cikls, kurā lietotājs ievada skaitli.
# Skaitli pagaidām varat noteikt paši.
# Programma pārbaude - vai skaitlis ir uzminēts.
# Ja nav uzminēts - izvada to, vai skaitlis ir lielāks, vai
# mazāks par minēto.
# Visas lietotāja ievades jāsaglabā sarakstā.
# Kad lietotājs ir uzminējis skaitli - izvadīt vārdu 'Uzvara'
# un visas lietotāja ievades.