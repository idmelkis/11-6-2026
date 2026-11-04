# Uzdevums: Izveidojat funkciju, kas pārbauda vai parole
# atbilst nosacījumiem - ir garāka par 5 simboliem, satur skaitli 
# (character.isnumeric() vai character.isdigit())
# un satur speciālu simbolu (character.isalnum()). 
def paroles_pārbaude(parole :str):
    garums = False
    skaitlis = False
    spec_simbols = False

    if len(parole) > 5:
        garums = True
    for simbols in parole:
        if simbols.isdigit():
            skaitlis = True
        if simbols.isalnum():
            spec_simbols = True
        # Ja mums jau ir atrasti gan cipari gan spec. simboli - varam ātrāk pārtraukt
        if skaitlis and spec_simbols:
            break
    return garums and skaitlis and spec_simbols
print(f'Parole Lavizes2A atbilst: {paroles_pārbaude("Lavizes2A")}')
print(f'Parole AVG1@! atbilst: {paroles_pārbaude("AVG1@!")}')
print(f'Parole Skola@ atbilst: {paroles_pārbaude("Skola@")}')
print(f'Parole avg atbilst: {paroles_pārbaude("avg")}')

# Veikala kods - 9_nodarbiba_veikals_original.py
# Uzdevums: Sadalīt kodu loģiskos funkciju blokos
# Sadalīts funkcijās - 9_nodarbiba_veikals_funkcijas.py

# Uzdevums: Izveidot funkciju no šī koda gabala
def kalkulators(skaitlis1, skaitlis2, darbības_zīme):
    rezultāts = 0
    if darbības_zīme == "+":
        rezultāts = skaitlis1 + skaitlis2
    elif darbības_zīme == "-":
        rezultāts = skaitlis1 - skaitlis2
    elif darbības_zīme == "*":
        rezultāts = skaitlis1 * skaitlis2
    elif darbības_zīme == "/":
        rezultāts = skaitlis1 / skaitlis2
    else:
        print("Nezināma darbība!")
        return None
    return rezultāts

rezultāts = kalkulators(10, 10, "+")
print(rezultāts)

skaitlis1 = float(input("Pirmais skaitlis: "))
skaitlis2 = float(input("Otrais skaitli: ")) # Float - daļskaitļi
darbības_zīme = input("Darbības zīme: ")
rezultāts = kalkulators(skaitlis1, skaitlis2, darbības_zīme)
print(f"Darbības {skaitlis1} {darbības_zīme} {skaitlis2} rezultāts: {rezultāts}")