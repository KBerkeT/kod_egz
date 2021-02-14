import math

print(
    """
    ******************************
    Gelişmiş Hesap Makinesi
    ******************************

    Çıkmak için 'q' ya basınız.

    İŞLEMLER

    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme
    5- Üs alma
    6- Kök alma
    7- Logaritma
    8- Faktöriyel
    9- Açı dönüşümleri
    10- Sayıyı yukarı yuvarla
    11- Sayıyı aşağı yuvarla
    12- Mutlak değer
    13- Mod alma
    14- Ortalama
    15- EBOB
    16- EKOK       
    """)

while True:

    islem = input("Lütfen bir işlem saçiniz : ")

    if islem == "q":
        print("Gelişmiş Hesap Makinesi kapatılıyor....")
        break

    elif islem == "1":
        print("""                 ***********************
                       Toplama İşlemi
                 ***********************
                 
Çıkmak için "q" ya basınız...""")
        toplam = 0
        while True:
            sayi = input("Sayı giriniz: ")
            if sayi == "q":
                print("Toplama işleminden çıkılıyor...")
                break
            toplam += float(sayi)
            print("Toplam =",toplam)

    if islem == "2":
        print("""
        **************
        Çıkarma işlemi
        **************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("Çıkarılan sayı :")
            if sayi == "q":
                print("Çıkarma işleminden çıkılıyor...")
                break
            cikan = float(input("Çıkan sayı :"))
            sonuc = float(sayi) - cikan
            print("Sonuç =",sonuc)

    if islem == "3":
        print("""
        ***************
        Çarpma İşlemi
        ***************
        
        Çıkmak için 'q' ya basınız...
        """)

        sonuc = 1
        while True:
            sayi = input("Sayı giriniz :")

            if sayi == "q":
                print("Çarpma işleminden çıkılıyor...")
                break
            sonuc *= float(sayi)
            print("Sonuç =",sonuc)

    if islem == "4":
        print(
        """
        *************
        Bölme İşlemi
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("Bölünen sayı :")
            if sayi == "q":
                print("Bölme işleminden çıkılıyor...")
                break

            bolen = float(input("Bölen sayı :"))
            sonuc = float(sayi)/bolen
            print("Sonuç =",sonuc)


    if islem == "5":
        print(
        """
        *************
        Üs alma İşlemi
        
        Çıkmak için 'q' ya basınız...
        *************
        """)

        while True:
            sayi = input("Üssü alınacak sayı :")
            if sayi == "q":
                print("Üs alma işleminden çıkılıyor...")
                break
            us = float(input("Üs :"))
            sonuc = float(sayi)**us
            print("{} ^ {} = {}".format(sayi,us,sonuc))


    if islem == "6":
        print(
        """
        *************
        Kök alma İşlemi
        
        Çıkmak için 'q' ya basınız...
        *************
        """)

        while True:
            sayi = input("Kökü alınacak sayı :")
            if sayi == "q":
                print("Kök alma işleminden çıkılıyor...")
                break
            kok = float(input("Kök kuvveti :"))
            sonuc = float(sayi)**(1/kok)
            print("Sonuç =",sonuc)

    if islem == "7":
        print(
        """
        *************
        Logaritma İşlemi
        
        Çıkmak için 'q' ya basınız...
        *************
        """)

        while True:
            sayi = input("Logaritması hesaplanacak sayı :")
            if sayi == "q":
                print("Logaritma işleminden çıkılıyor...")
                break
            taban = float(input("Taban :"))
            sonuc = math.log(float(sayi),taban)
            print("Logaritma {} tabanında {} = {}".format(sayi,taban,sonuc))

    if islem == "8":
        print(
        """
        *************
        Faktöriyel İşlemi
        
        Çıkmak için 'q' ya basınız...
        *************
        """)

        while True:
            sayi = input("Faktoriyel hesaplanacak sayı :")
            if sayi == "q":
                print("Faktoriyel işleminden çıkılıyor...")
                break
            sonuc = math.factorial(float(sayi))
            print("Faktoriyel({}) = {}".format(sayi,sonuc))

    if islem == "9":
        print(
        """
        *************
        Açı Dönüşümleri 
        *************
        
        Dönüşümler:
        
        1- Derece --> Radyan
        2- Radyan --> Derece
        
        Çıkmak için 'q' ya basınız...
        """)
        while True:
            donusum = input("Lütfen bir dönüşüm seçiniz : ")
            if donusum == "q":
                print("Dönüşüm işleminden çıkılıyor...")
                break
            elif (donusum == "1"):
                print("""DERECE --> RADYAN""")
                sayi = float(input("Lütfen sayınızı DERECE cinsinden giriniz : "))
                sonuc = math.radians(sayi)
                print("{} derece = {} radyan".format(sayi,sonuc))
            elif (donusum == "2"):
                print("""RADYAN --> DERECE""")
                sayi = float(input("Lütfen sayınızı RADYAN cinsinden giriniz : "))
                sonuc = math.degrees(sayi)
                print("{} radyan = {} derece".format(sayi,sonuc))

    if islem == "10":
        print(
        """
        *************
        Sayıyı yukarı yuvarla 
        
        Çıkmak için 'q' ya basınız...
        *************
        """)

        while True:
            sayi = input("Ondalıklı sayı giriniz :")
            if sayi == "q":
                print("Yuvarlama işleminden çıkılıyor...")
                break
            sonuc = math.ceil(float(sayi))
            print(sonuc)

    if islem == "11":
        print(
        """
        *************
        Sayıyı aşağı yuvarla
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("Ondalıklı sayı giriniz :")
            if sayi == "q":
                print("Yuvarlama işleminden çıkılıyor...")
                break
            sonuc = math.floor(float(sayi))
            print(sonuc)

    if islem == "12":
        print(
        """
        *************
        Mutlak değer İşlemi
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("Mutlak değeri alınacak sayı :")
            if sayi == "q":
                print("Mutlak işleminden çıkılıyor...")
                break
            sonuc = math.fabs(float(sayi))
            print(sonuc)


    if islem == "13":
        print(
        """
        *************
        Mod alma İşlemi
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("Modu alınacak sayı :")
            if sayi == "q":
                print("Mod işleminden çıkılıyor...")
                break
            sonuc = math.fmod(float(sayi))
            print(sonuc)

    if islem == "14":
        print(
        """
        *************
        Ortalama İşlemi
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        kume = []
        print("Ortalamsı alınacak sayıların hepsi girilince q ya basınız..")
        while True:
            sayi = input("Ortalamsı alınacak sayılar:")
            if sayi == "q":
                break
            kume.append(float(sayi))

        toplam = 0
        for i in kume:
            toplam += i
        sonuc = toplam / len(kume)
        print("Ortalama =",sonuc)

    if islem == "15":
        print(
        """
        *************
        EBOB İşlemi
        *************
        
        Çıkmak için 'q' ya basınız...
        """)

        while True:
            sayi = input("1.sayı :")
            if sayi == "q":
                print("EBOB işleminden çıkılıyor...")
                break
            sayi2 = int(input("2.sayı :"))
            sonuc = math.gcd(int(sayi),sayi2)

            print("EBOB({},{}) = {}".format(sayi,sayi2,sonuc))

