#a = deltaV / deltaT
#f(V, T) = V/T

# Funkciju pieraksts:
# def <nosaukums>(<parametri>):
# ----|darbība
# nosaukumam tādi paši nosacījumi kā mainīgo nosaukumiem, t.i.
# nevar sākties ar skaitli, nevar būt spec. simboli atskaitot apakšsvītru
def nosaukums(parametrs):
    pass

def paātrinājums(V, T):
    return V/T # atgriež vērtību, kuru var piešķirt mainīgajam
rezultāts = paātrinājums(10, 2)
print(rezultāts)

# Kad lietot funkcijas
# 1. Ja atkārtojas kods vairākas reizes (piem 3+)
# 2. Lai padarītu kodu lasāmāku - izdala loģiku individuālos blokos
# piemēram - 
# def ievades_bloks():
#     ievade = int(input("Ievade"))
#     if ievade == 1:
#         return "Kaut ko"
#     elif ievade == 2:
#         return "Cita lieta"
# def apstrādes_bloks(ievade):
#     pass
# while True:
#     rezultāts = ievades_bloks()
#     apstrādes_bloks(rezultāts)
# 3. Abstraktēšana - Kāda koncepta/procesa aprakstīšana (vairāk saistīts ar objektorientēto programmēšanu)
# Piem. procesam - datora ieslēgšana - def datoraIeslēgšana()...

# Ir divu veidu funcijas
# Procedūrām - Funckijas kas neatgriež vērtību, bet veic darbību
# Piemērs - print() - veic darbību (izvada tekstu, neatgriež vērtību)
# Funkcija - Funckijas kas atgriež vērtību
# Piemērs - input() - atgriež ievadīto tekstu, random.randint() - atgriež nejaušu vērtību

# Uzdevums: Uzrakstat procedūru, kas pārbauda vai ievadītais skaitlis ir 
# lielāks, mazāks vai vienāds ar 0 - un izvada to.
# piem. pārbaudīt_skaitli(0) izvada "skaitlis ir 0"
def pārbaudīt_skaitli(skaitlis):
    if skaitlis > 0:
        print("Lielāks")
    elif skaitlis < 0:
        print("Mazāks")
    else:
        print("Skaitlis ir 0")
# ievade = int(input("Skaitlis: "))
# pārbaudīt_skaitli(ievade)
# pārbaudīt_skaitli(ievade) # Mēs 1 funkciju varam izsaukt vairākas reizes
# pārbaudīt_skaitli(ievade)

# Uzdevums: Uzrakstīt funkciju kas atgriež True, ja skaitlis ir pāra
# vai False, ja skaitlis ir nepāra (skaitlis % 2 == 0)
def ir_pāra(skaitlis):
    if skaitlis % 2 == 0:
        return True
    else:
        return False
print(ir_pāra(10))
print(ir_pāra(19))

# Funkcijas ar vairākiem parametriem
def vairāki_parametri(param1, param2, param3): # vairākus parametrus varam atdalīt ar komatu
    print(param1, param2, param3)
vairāki_parametri("1", "2", "3")

# pozicionālie parametri - izsaucot varam norādīt nosaukumu parametram
vairāki_parametri(param1="Pirmais", param2="Otrais", param3="Trešais")

# Neobligātie parametri - parametri, kuriem ir jau norādīta standarta vērtība
def std_vērtība(param1 = "Pirmais", param2 = "Otrais", param3 = "Trešais"):
    print(param1, param2, param3)
std_vērtība() # Varam izsaukt funkciju nenorādot vērtības, izvada - Pirmais Otrais Trešais
std_vērtība(param2="Izmainīta vērtība") # Varam izmainīt definēto standarta vērtību. Izvada - Pirmais Izmainīta vērtība Trešais

# typedef - norāda datu tipus mainīgajiem - nav obligāti, Python to neuzspiež
def typedef (mainīgais :int) -> str: # :int - mainīgais ir ar datu tipu int, -> str - atgriež str
    """
    Šeit ir funkcijas apraksts
    Lai to redzētu - iekš vs code izsaucam funkciju un uzliekam virsū peli
    """
    return str(mainīgais)
typedef(0)

# Neierobežots daudzums parametru:
# piem. - print("Parametrs 1", "Parametrs 2")
def inf_params(*parametri): # Pievienojam zvaigznīti pie mainīgā nosaukuma
    print(parametri) # Visi parametri tiek ievietoti kortežā/sarakstā (Tuple)
inf_params("Parametrs 1", "Parametrs 2", "Parametrs 3")

# Uzdevums: Uzrakstīt funkciju, kas pieņem neierobežotu daudzumu skaitļus
# Un izvadīt lielāko skaitli. Neizmantojat iebūvēto funkciju max().
def lielākais_skaitlis(*skaitļi):
    rezultāts = skaitļi[0]
    for skaitlis in skaitļi:
        if skaitlis > rezultāts:
            rezultāts = skaitlis
    return rezultāts
print(lielākais_skaitlis(10,20,30,40))
print(lielākais_skaitlis(-1,9,-2,5))

# Rekursīvās funkcijas - funkcijas, kas izsauc sevi
# piemērs
def faktoriālis(skaitlis):
    print(f"Izsaukts ar skaitli {skaitlis}")
    if skaitlis == 0 or skaitlis == 1:
        return 1
    return skaitlis * faktoriālis(skaitlis - 1)
print(faktoriālis(10))