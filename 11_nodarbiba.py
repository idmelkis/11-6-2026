saraksts = [ "vērtība", "vērtība2" ]
saraksts[0]

# Vārdnīca - glabā vairākus datus iekš viena mainīgā
# Piekļuvei izmanto atslēgu - arī jūsu dota vērtība
# kas norāda uz noteiktu vērtību vārdnīcā.
vārdnīca = {
    "atslēga": "asdas3e5678",
    0: "skaitlis",
    True: False
}
print(vārdnīca["atslēga"])
print(vārdnīca[0])

lietotājs1 = {
    "lietotājvārds": "Jānis",
    "parole": "12345"
}
lietotājs2 = {
    "lietotājvārds": "Pēteris",
    "parole": "12345"
}
datubāze = [lietotājs1, lietotājs2]

# Pievienot datus
vārdnīca = {"eksitējoša_vērtība": "oriģinālā vērtība"}
# 1. variants - update funkcija
vārdnīca.update({"jauna_atslēga": "jauna vērtība"})
# Eksistējošas vērtības tiks pārrakstītas
vārdnīca.update({"eksitējoša_vērtība": "jaunā vērtība"})
# 2. variants - piešķirt pa tiešo
vārdnīca["vēl_jauna_atslēga"] = "trešā vērtība"
print(vārdnīca)

# Izņemt datus
# 1. varians - pop funkcija
vārdnīca.pop("eksitējoša_vērtība")
# 2. variants - del atslēgvārds
del vārdnīca["jauna_atslēga"]
print(vārdnīca)

# Piekļūt datiem
for iii in range(0,10):
    vārdnīca[iii] = f"vērtība{iii}"
# 1. Piekļūt atslēgas vērtībai - vārdnīca[atslēga]
print(vārdnīca["vēl_jauna_atslēga"]) # izvada 'trešā vērtība'
print("================== Atslēgas")
# 2. Piekļūst visām atslēgām - .keys()
#print(vārdnīca.keys())
# var izmantot iekš for cikla
for atslēga in vārdnīca.keys():
    print(atslēga)
# 3. Piekļūst visām vērtībām .values()
print("================== Vērtības")
#print(vārdnīca.values())
# var izmantot iekš for cikla
for vērtība in vārdnīca.values():
    print(vērtība)
# 4. Piekļūt visiem atslēgu <-> vērtību pāriem
print("================== Abi")
for atslēga, vērtība in vārdnīca.items():
    print(f"atslēga: {atslēga}, vērtība: {vērtība}")

# Praktisks uzdevums: Dota vārdnīca ar vērtībām
vārdnīca = {
    0: 10,
    2: 34,
    3: 56,
    "teksts": 67
}
# Izvadīt visas vērtība reizinātas * 2
for vērtība in vārdnīca.values():
    print(vērtība*2)

# Uzdevums: Dots kods, kas ģenerē sarakstu ar 20 vērtībām, 
# kurā atslēgas ir skaitļi no 0 līdz 20, un vērtības ir nejauši skaitļi
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 1000)
print(vardnica)
# Izdzēst katru otro atslēgu-vērtību pāri no šīs vārdnīcas
# Lai iegūtu saraksta lielumu, var izmantot len() funkciju.
for idx in range(0,len(vardnica.items())):
    if idx % 2 == 0:
        del vardnica[idx]
print(vardnica)

# Uzdevums: Dots saraksts ar vārdnīcām
automašīnas = [
    {"modelis": "Audi A4", "ātrums": 240},
    {"modelis": "Toyota Corolla", "ātrums": 180},
    {"modelis": "Tesla Model 3", "ātrums": 250}
]
# Izvadāt automašīnas kuru ātrums > 200km/h
for auto in automašīnas:
    if auto["ātrums"] > 200:
        print(auto['modelis'])

# Uzdevums (procentu darbs):
# Izveidojat divus mainīgos - svars un distance
# Uzrakstāt divas funkcijas kas pielieto šos mainīgos - 
# 1) aprēķināt piegādi un 2) izvadīt piegādes tipu

# 1) Aprēķināt piegādi; izvada piegādes cenu, kas tiek aprēķināti šādi - 
# Svars līdz 2kg - EUR3
# Svars no 2 līdz 5kg - EUR5
# Svars > 5kg - EUR8
# Tad pievieno EUR0.10 par katru kilometru

# 2) Piegādes tips izvada 
# 'Vietējā' ja distance < 10km
# 'Reģionālā' ja distance ir 10-50km
# 'Gara distance' ja distance >50km

# Izsaucat šīs funkcijas ar testa datiem.