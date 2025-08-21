#task 1
print("""
Welcome my Calculator
1) a + b
2) a - b
3) a * b
4) a / b
\n
""")
secim = int(input("eded daxil edin"))

eded1 = float(input("birinci ededi daxil edin"))
eded2 = float(input("ikinci ededi daxil edin"))

if secim == 1:
    print(eded1 + eded2)
elif secim == 2:
    print(eded1 - eded2)
elif secim == 3:
    print(eded1 * eded2)
elif secim == 4:
    if eded2 == 0:
        print("Error")
else:
    print(eded1 / eded2)
#task 3
sifre = input("kodu daxil edin")
sifre2 = "12345"
if sifre == sifre2:
    print("Xos Gelmisiniz")
else:
    print("Sifre yalnisdir")