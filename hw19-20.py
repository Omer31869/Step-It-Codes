pul = 3000

while True:
    print("1) Balansı göstər")
    print("2) Balansa pul əlavə et")
    print("3) Balansdan pul çıxar")
    print("4) Proqramdan çıxış")

    secim = input("Zehmet olmasa Seçiminizi daxil edin (1-4): ")

    if secim == "1":
        print(f"Sizin balans: {pul} AZN")
    elif secim == "2":
        miqdar = int(input("Ne qeder elave etmek isteyirsiniz? "))
        pul += miqdar
        print(f"Yeni balans: {pul} AZN")
    elif secim == "3":
        miqdar = int(input("Ne qeder lazimdir? "))
        if miqdar > pul:
            print("Kifayet qeder mebleg yoxdur.")
        else:
            pul -= miqdar
            print(f"Yeni balans: {pul} AZN")
    elif secim == "4":
        print("Sag Olun!")
        break
    else:
        print("Yanlish secim. Zehmet olmasa 1-4 arasi reqem daxil edin.")
