# Jāuzraksta cikls, kurā lietotājs ievada skaitli.
# Skaitli pagaidām varat noteikt paši.
# Programma pārbaude - vai skaitlis ir uzminēts.
# Ja nav uzminēts - izvada to, vai skaitlis ir lielāks, vai
# mazāks par minēto.
# Visas lietotāja ievades jāsaglabā sarakstā.
# Kad lietotājs ir uzminējis skaitli - izvadīt vārdu 'Uzvara'
# un visas lietotāja ievades.
# skaitlis = 50
# minējumi = []
# while True:
#     minējums = int(input("Minējums: "))
#     minējumi.append(minējums)
#     if minējums > skaitlis:
#         print("Minējums ir lielāks")
#     elif minējums < skaitlis:
#         print("Minējums ir mazāks")
#     else:
#         break
# print("Uzvara")
# print(minējumi)

# Uzdevums: Uzrakstāt programmu, kurā lietotājs ievada skaitli n,
# Un programma izvadīs n rindas ar zvaigznītēm (*), sākot ar 1 zvaigzni
# pirmajā rindā līdz n zvaigznītēm n rindā, piem.
# Ievade: 4
# *
# **
# ***
# ****
# for variants:
# n = int(input("Ievade: "))
# for iii in range(1, n + 1):
#     print(iii * "*")
# # while variants
# n = int(input("Ievade: "))
# skatitajs = 0
# while skatitajs < n + 1:
#     skatitajs += 1
#     print(skatitajs * "*")

# % - modulus operators
# izmanto lai iegūtu dalījuma atlikumu
# 6 % 3 == 0
# 7 % 3 == 1
# Parasti izmanto lai pārbaudītu vai skaitlis dalās ar citu (atlikums ir 0)

# Uzdevums: Uzrakstīt ciklu, kas iet pāri skaitļiem no 1 līdz 100
# Ja skaitlis dalās ar 3 - izvadat vārdu "Fizz"
# Ja skaitlis dalās ar 5 - izvadat vārdu "Buzz"
# Ja skaitlis dalās gan ar 3, gan ar 5 - izvadat vārdu "FizzBuzz"
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem - izvadāt šo skaitli
# Izvades piemērs: 1, 2, Fizz, 4, Buzz...

for iii in range(1, 101):
    #if iii % 3 == 0 and iii % 5 == 0:
    if iii % 15 == 0:
        print("FizzBuzz")
    elif iii % 3 == 0:
        print("Fizz")
    elif iii % 5 == 0:
        print("Buzz")
    else:
        print(iii)

# Uzdevums: Izvadāt 5*5 reizināšanas tabulu (izmantojam ciklus)
# Hint - cikls ciklā
# piem. ar 3*3
# 1 2 3
# 2 4 6
# 3 6 9
izmērs = 5
for iii in range(1, izmērs + 1):
    for jjj in range(1, izmērs + 1):
        print(iii*jjj, end=" ") # end - pēc print netiks pievienota jauna rinda
    print() # tukšs print - jauna rinda

# Uzdevums: Uzrakstāt programmu, kas pārbauda vai skaitlis ir pirmskaitlis
# Pirmskaitlis ir skaitlis kas dalās tikai ar 1, vai sevi.
skaitlis = int(input("Skaitlis: "))
nav_pirmskaitlis = False
for iii in range(2, skaitlis):
    if skaitlis % iii == 0:
        print("Nav pirmskaitlis")
        nav_pirmskaitlis = True
if not nav_pirmskaitlis:
    print("Ir pirmskaitlis")