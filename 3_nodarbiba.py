# Uzdevums: Prasāt lietotājam lai ievada 
# tā mīļāko dzīvnieku, ēdienu un valsti.
# Izvadat šo informāciju sekojošā formātā:

# Mīļākie:
# Dzīvnieks: {}
# Ēdiens: {}
# Valsts: {}
# dzivnieks = input("Ievadat mīļāko dzīvnieku: ")
# ediens = input("Ievadat mīļāko ēdienu: ")
# valsts = input("Ievadat mīļāko valsti: ")
# print("Mīļākie:")
# print(f"Dzīvnieks: {dzivnieks}")
# print(f"Ēdiens: {ediens}")
# print(f"Valsts: {valsts}")

# Uzdevums: Ir dots sekojošs saraksts
soma = [ "Zobens", "Vairogs", "Ūdens" ]
# Uzrakstat programmu, kas - ļauj lietotājam izņemt vienu no elementiem no somas
# Izvadat izņemto elementu, un somas saturu pēc izņemšanas.
# Ir divi varianti - vai nu ar list.pop(idx), vai list.remove(str)!
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# iznemt_elementu = input("Ko izņemt? ")
# print(f"Tiks izņemts {iznemt_elementu}...")
# soma.remove(iznemt_elementu)
# print(f"Somas saturs pēc izņemšanas: {soma}")
####
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# iznemt_kārtu = input('Ko pēc kārtas izņemt? ') # input atgriež tekstu! idx ir skaitlis.
# iznemt_idx = int(iznemt_kārtu) # int() pārveido tekstu par skaitli.
# print(f"Tiks izņemts {soma[iznemt_idx]}...")
# soma.pop(iznemt_idx)
# print(f"Somas saturs pēc izņemšanas: {soma}")

# if <loģiskā pārbaude>:
#    | darbības

# loģiskās pārbaudes -
# == - vai ir vienāds ar labo pusi
# != - vai nav vienāds ar labo pusi
# > - kreisā puse lielāka par labo
# < - kreisā puse mazāka par labo
# >= - kreisā puse lielāka vai vienāda par labo
# <= - kreisā puse mazāka vai vienāda par labo
# is - ir vienāds ar
# is not - nav vienāds ar

# mainīgais = int(input("Ievadat skaitli"))
# if mainīgais == 11:
#     print("Izpildās tikai, ja mainīgais ir 11")
# elif mainīgais == 12: # elif = else if
#     print("Izpildās tikai, ja mainīgais ir 12")
# else:
#     print("Nekas no iepriekšējā neizpildās")

# Uzdevums: Lietotājam jāievada skaitlis, un programmai ir jāizvada 
# "Jā", ja skaitlis ir MAZĀKS par 10, "Nē", ja skaitlis ir lielāks par 10.
# mainīgais = int(input("Ievadat skaitli"))
# if mainīgais > 10:
#     print("Nē")
# else: # elif mainīgais <= 10:
#     print("Jā")

# Loģisko pārbaužu apvienošana
# and -- jāizpildās abām pusēm (True AND True)
# or -- Jāizpildās vismaz vienai no pusēm (True Or False)
mainīgais_1 = 10
mainīgais_2 = 20
if mainīgais_1 == 10 and mainīgais_2 == 20: # Izpildās tikai ja abi ir patiesi
    print("AND Patiess")
if mainīgais_1 == 10 or mainīgais_2 == 20: # Izpildās ja viens ir patiess
    print("OR Patiess")

# Uzdevums: Izveidojat biļešu cenu kalkulatoru
# Bērniem zem 12 gadiem, cena ir €5
# Skolēniem (12-17), cena ir €8
# Pieaugušajiem (18-65), cena ir €15
# Senioriem (65+), cena ir €8
# Lietotājam jāievada vecums un programmai ir jāizvada biļetes cena.
vecums = int(input("Ievadat vecumu"))
cena = 0
if vecums < 12:
    cena = 5
elif vecums >= 12 and vecums <= 17:
    cena = 8
elif vecums >= 18 and vecums <= 64:
    cena = 15
else:
    cena = 8
print(f"Biļetes cena: {cena}!")