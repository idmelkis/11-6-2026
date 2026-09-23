# Uzdevums: Kalkulators
# Lietotājam jāievada divi skaitļi un darbības zīme
# (piem. saskaitīšana, atņemšana, dalīšana vai reizināšana)
# Un programmai ir jāizvada darbības rezultāts
# skaitlis1 = float(input("Pirmais skaitlis: "))
# skaitlis2 = float(input("Otrais skaitli: ")) # Float - daļskaitļi
# darbības_zīme = input("Darbības zīme: ")
# rezultāts = 0
# if darbības_zīme == "+":
#     rezultāts = skaitlis1 + skaitlis2
# elif darbības_zīme == "-":
#     rezultāts = skaitlis1 - skaitlis2
# elif darbības_zīme == "*":
#     rezultāts = skaitlis1 * skaitlis2
# elif darbības_zīme == "/":
#     rezultāts = skaitlis1 / skaitlis2
# else:
#     print("Nezināma darbība!")
# print(f"Darbības {skaitlis1} {darbības_zīme} {skaitlis2} rezultāts: {rezultāts}")

# switch / match-case - pieejams tikai sākot no Python 3.10
# Izmanto kā alternatīvu if, situācijās ja ir viens mainīgais kuram var būt
# dažādas vērtības
# match darbības_zīme:
#     case "+":
#         rezultāts = skaitlis1 + skaitlis2
#     case "-":
#         rezultāts = skaitlis1 - skaitlis2
#     case "*":
#         rezultāts = skaitlis1 * skaitlis2
#     case "/":
#         rezultāts = skaitlis1 / skaitlis2
#     case _:
#         print("Nezināma darbība!")

# Cikli
# While - Izmanto vispārējos gadījumos
# For - Izmanto lai ietu pāri sarakstiem

# For
saraksts = [ 123, 234, 456, 567 ]
# Iterācija - viena reize, kurā tiek palaistas visas darbības ciklā
for vērtība in saraksts: 
    # piem. katrā iterācijā tiek palaists viens print()
    print(vērtība)

# range() - atgriež skaitļus diapazonā
# parametri - sākums, beigas, solis
# (piem. ja gribētu katru otro skaitli - skaitlis būtu 2)
for iii in range(0,10,2): # diapazons - [0,10)
    print(iii)

# Uzdevums: Uzrakstat ciklu, kurš atrod sarakstā 'saraksts'
# lietotāja ievadītu skaitli. Atgriežat 'nav', ja tas sarakstā nav.
# Izvadat vērtību, ja tā ir atrasta.
saraksts = [ 123, 234, 456, 567 ]
meklejamais = int(input("Meklējamais skaitlis: "))
# for
atrasts = False
for vertiba in saraksts:
    if vertiba == meklejamais:
        print(meklejamais)
        atrasts = True
if not atrasts: # if atrasts == False:
    print("Nē")
# while
atrasts = False
pasreizejais_idx = 0
while not atrasts:
    if saraksts[pasreizejais_idx] == meklejamais:
        print(saraksts[pasreizejais_idx])
        atrasts = True
    pasreizejais_idx += 1
    if len(saraksts) == pasreizejais_idx:
        break # pārtrauc ciklu
if not atrasts: # if atrasts == False:
    print("Nē")

# Svarīgi atslēgvārdi
# break - pārtrauc ciklu
# continue - beidz iterāciju, sākot nākošo
a = 0
while a < 15:
    a += 1
    # ja a ir 5, mēs beidzam iterāciju ar continue pirms 'print' 
    # un sākam nākošo tādējādi efektīvi izlaižot šo iterāciju
    if a == 5:
        continue
    # ja a ir 9, mēs beidzam ciklu ar break
    if a == 9:
        break
    print(a)

# Uzdevums: Uzrakstat for ciklu, kas ļauj ievadīt sarakstā 3 jebkādas vērtības
saraksts = []
for iii in range(3):
    saraksts.append(input("Ievade: "))
print(f"Ievadītais saraksts: {saraksts}")

# Uzdevums: Uzrakstat šo darbību izmantojot while ciklu
saraksts = []
indekss = 0 # Manuāli sekojam līdzi pievienoto elementu skaitam
while indekss < 3:
    saraksts.append(input("Ievade: "))
    indekss += 1 # indekss = indekss + 1
print(f"Ievadītais saraksts: {saraksts}")
# VAI
saraksts = []
while len(saraksts) < 3:
    saraksts.append(input("Ievade: "))
print(f"Ievadītais saraksts: {saraksts}")