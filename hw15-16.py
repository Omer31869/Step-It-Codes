eded = input("Bir ədəd daxil et: ")
say = 0
cem = 0
for reqem in eded:
    cem += int(reqem)
    say += 1
print("Reqemlerin sayı:", say)
print("Reqemlerin cemi:", cem)

#task 2
eded = input("Bir eded daxil et: ")
eded2 = ""
for simvol in eded:
    eded2 = simvol + eded2
print("Eksine çevrilmiş ədəd:", eded2)

#task3
i = 0
musbet = 0
menfi = 0
sifir = 0

while i < 10:
    eded = int(input("Eded daxil et: "))
    if eded > 0:
        musbet += 1
    elif eded < 0:
        menfi += 1
    else:
        sifir += 1
    i += 1

print("Musbet faiz:", musbet * 10, "%")
print("Menfi faiz:", menfi * 10, "%")
print("Sıfır faiz:", sifir * 10, "%")

#task4
i = 0
cut = 0
tek = 0

while i < 10:
    eded = int(input("Eded daxil et: "))
    if eded % 2 == 0:
        cut += 1
    else:
        tek += 1
    i += 1

print("Cut faiz:", cut * 10, "%")
print("Tek faiz:", tek * 10, "%")

#task5 -




