# Datu tipi:
# Teksts - String
#   Teksts + Skaitlis būs kļūda
#   "5" + 5 = Kļūda
#   Teksts * Skaitlis - teksts tiks reiznāts n reizes
#   "5" * 5 = "55555"
# Skaitļi - Integer
# Daļskaitļi - Float/Double
# Loģiskie predikāti Patiess/Nepatiess - Boolean (True/False)
# Saraksti - List

rezultāts = "asdasd" == "asdasd" # rezultāts = True
rezultāts = "asdasd" == "dsadas" # rezultāts = False
print(rezultāts) # Izvada False
rezultāts = 4 * 4
rezultāts = "1" * 5
print(rezultāts)

print("*" * 10)
print("Uzdevuma rezultāts")
print("*" * 10)

# Lai apvienotu tekstu ar skaitli - skaitli var ielikt funkcijā str
rezultāts = "10 * 10 = " + str(10*10)
# Formatētie string - pirms pirmās pēdiņas parādās burts f
# Viss kas ir iekš pēdiņām kvadrātiekavās tiek pārveidots par tekstu
rezultāts = f"10 * 10 = {10 * 10}"
rezultāts = f"10 * 10 | {rezultāts} | {rezultāts} | {5 * 5}"
print(rezultāts)
#print(f"10 * 10 | {rezultāts} | {rezultāts} | {5 * 5}")

# Uzdevums - ievadat divus mainīgos -
# Vārds, uzvārds
# Izvadat - "Sveiks {Vārds}, {Uzvārds}!"
# vārds = input("Vārds: ")
# uzvārds = input("Uzvārds: ")
# print(f"Sveiks {vārds}, {uzvārds}!")

# Teksts vairākās rindās 
# \n - speciāls simbols kas pārnes tekstu jaunā rindā
print(f"Pirmā rinda\nOtrā rinda\nTrešā rinda")
# Trīs pēdiņas - teksts tiks izvadīts burtiski - ieskaitot jaunas rindas simbolus
print("""Pirmā rinda
Otrā rinda
Trešā rinda""")

# Saraksti - izmanto lai glabātu līdzīgu informāciju vienā mainīgajā
saraksts = [ "vērtība 1", "vērtība 2", 10, 5*5, True, rezultāts ]
# Piemēram - dati no kāda fizikas sensora - katru sekundi tiek iegūts skaitlis
laiksērijas_dati = [ 10, 20, 30, 40, 30, 20, 10 ]
saraksts = [ [10, 20, 30], [30, 40, 50], [60, 70, 80] ]
print(saraksts)

# Saraksti tiek indeksēti sākot no 0, t.i. pirmais elements ir 0 indekss
saraksts = [[10, 20, 30], [30, 40, 50], [60, 70, 80]]
#jauna_vērtība = int(input("Ievade: "))
# saraksts.append(jauna_vērtība) # Pievieno galā
# saraksts.insert(0, jauna_vērtība) # Pievieno sākumā
print(saraksts)
#saraksts.remove([10, 20, 30]) # Izņem vērtību [10, 20, 30] no saraksta
#saraksts.remove(jauna_vērtība) # Izņem mainīgā jauna_vērtība vērtību no saraksta
# N.B. šis notiek tikai 1x, ja vērtība parādās vairākas reizes - .remove() jālaiž
# vairākas reizes.

saraksts.pop(0) # Izņem pirmo vērtību no saraksta 
saraksts.pop(-1) # Izņem pēdējo vērtību no saraksta
#saraksts.pop(-2) # Izņem pirmspēdējo vērtību no saraksta
print(saraksts)

vēlviens_saraksts = ("123", "44") # Tuple - to nevar izmainīt pēc izveides
# Praktisks pielietojums - Peles koordinātes (x,y) - 
# Tās mainās katru reizi kad kustinat peli
# Bet jūs tās varat tikai nolasīt - ne izmainīt
cits_saraksts = ["123", "44"]
print(len(cits_saraksts))
teksts = "Šis ir teksts"
print(len(teksts)) # Teksts arī ir sava veida saraksts - viss ko darām ar sarakstiem varām darīt ar tekstu

print(cits_saraksts[-1]) # Izvada pēdējo saraksta elementu
print(teksts[-2]) # Izvada pirmspēdējo burtu
print(teksts[0:2]) # Izvada burtus ar 0 un 1 indeksiem - intervāls ir no 0 LĪDZ noteiktajam indeksam.
