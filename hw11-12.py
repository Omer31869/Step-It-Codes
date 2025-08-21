#task1
qiymet = float(input("Qiyməti daxil edin: "))
qram = float(input("Qramı daxil edin: "))

if (qram >= 0 and qram < 100):
    endirim = 0
elif (qram >= 100 and qram < 200):
    endirim = qiymet * 0.3
elif (qram >= 200 and qram < 300):
    endirim = qiymet * 0.5
elif (qram >= 300):
    endirim = qiymet * 0.7
else:
    endirim = 0

yeni_qiymet = qiymet - endirim
print("Endirimli qiymət:", yeni_qiymet)
#task2
ay = int(input("Ayı daxil et: "))
gun = int(input("Günü daxil et: "))

if (ay == 1 and gun <= 19 or ay == 12 and gun >= 22):
    print("Oğlaq")
elif (ay == 1 and gun >= 20 or ay == 2 and gun <= 18):
    print("Dolça")
elif (ay == 2 and gun >= 19 or ay == 3 and gun <= 20):
    print("Balıq")
elif (ay == 3 and gun >= 21 or ay == 4 and gun <= 19):
    print("Qoç")
elif (ay == 4 and gun >= 20 or ay == 5 and gun <= 20):
    print("Buğa")
elif (ay == 5 and gun >= 21 or ay == 6 and gun <= 20):
    print("Əkizlər")
elif (ay == 6 and gun >= 21 or ay == 7 and gun <= 22):
    print("Xərçəng")
elif (ay == 7 and gun >= 23 or ay == 8 and gun <= 22):
    print("Şir")
elif (ay == 8 and gun >= 23 or ay == 9 and gun <= 22):
    print("Qız")
elif (ay == 9 and gun >= 23 or ay == 10 and gun <= 22):
    print("Tərəzi")
elif (ay == 10 and gun >= 23 or ay == 11 and gun <= 21):
    print("Əqrəb")
elif (ay == 11 and gun >= 22 or ay == 12 and gun <= 21):
    print("Oxatan")
else:
    print("Yanlış ay və ya gün")
#task3
yas = int(input("Yaşınızı daxil edin: "))
cins = input("Cinsinizi daxil edin (K/Q): ")

if (cins == "K" and yas >= 65):
    print("Təqaüd yaşıdır")
elif (cins == "Q" and yas >= 60):
    print("Təqaüd yaşıdır")
else:
    print("Təqaüd yaşı deyil")
#task4
il = int(input("İli daxil et: "))

if (il % 400 == 0 or il % 4 == 0 and il % 100 != 0):
    print("Uzun ildir")
else:
    print("Uzun il deyil")



