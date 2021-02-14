print("""**************************************
Hesap Makinesi Programı 

İşlemler:

1.Toplama işlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4.bölme işlemi

**************************************
""")

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))

islem = input("İşlem giriniz:")

if islem == "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} in toplamı {} dir.".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} in toplamı {} dir.".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} in toplamı {} dir.".format(a, b, a / b))
else:
    print("Geçersiz işlem.")