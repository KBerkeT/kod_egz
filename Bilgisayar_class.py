import random
import time

class Bilgisayar():

    def __init__(self,pc_durum = "Kapalı",pc_ses = 0,uygulamalar = ["Belgelerim"]):

        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.uygulamalar = uygulamalar

    def pc_ac(self):
        if self.pc_durum == "Açık":
            print("Bilgisayar zaten açık...")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum = "Açık"

    def pc_kapat(self):
        if self.pc_durum == "Kapalı":
            print("Bilgisayar zaten kapalı...")
        else:
            print("Bilgisayar kapanıyor...")
            self.pc_durum = "Kapalı"

    def ses_ayar(self):
        print("Ses açmak için    : + "
              "Ses azaltmak için : - "
              "Ses ayarlarından çıkmak için 'q' ya basınız.")

        while True:
            islem = input("Bir işlem seçiniz:")

            if islem == "+":
                if self.pc_ses < 32:
                    self.pc_ses += 1
                    print("Ses:",self.pc_ses)
            elif islem == "-":
                if self.pc_ses > 0:
                    self.pc_ses -= 1
                    print("Ses:",self.pc_ses)
            elif islem == "q":
                print("Ses ayarlarından çıkılıyor."
                      "Ses :",self.pc_ses)
                break
            else:
                print("Lütfen geçerli bir işlem seçiniz...")

    def yeni_uygulama(self,uygulama_ismi):
        print("Uygulama yükleniyor...")
        time.sleep(1)
        self.uygulamalar.append(uygulama_ismi)
        print("Uygulama yüklendi...")

    def uygulama_sil(self,silinecek_uyg):
        for i in self.uygulamalar:
            if i == silinecek_uyg:
                print("Uygulama siliniyor...")
                time.sleep(1)
                self.uygulamalar.remove(i)
                print("{} uygulaması silindi...".format(silinecek_uyg))
            else:
                print("Böyle bir uygulama bulunmuyor...")

    def rastgele_uyg(self):
        rastgele = random.randint(0,len(self.uygulamalar)-1)
        yeni_uyg = self.uygulamalar[rastgele]
        print("Açılan uygulama {}".format(yeni_uyg))

    def __len__(self):
        return len(self.uygulamalar)

    def __str__(self):
        return "Bilgisayar durumu : {}\nSes seviyesi : {}\nUygulamalar : {}".format(self.pc_durum,self.pc_ses,self.uygulamalar)

bilgisayar = Bilgisayar()

print(
"""
***************

Bilgisayar Uygulaması

***************

1 - PC aç
2 - PC kapat
3 - Ses ayaları
4 - Yeni uygulama yükle
5 - Uygulama sil
6 - Rasgele uygulama aç
7 - Uygulama sayısı gösterme
8 - Bilgisayar Bilgileri

Çıkmak için 'q' ya basınız...
""")

while True:
    islem = input("Bir işlem seçiniz : ")

    if (islem == "q"):
        print("Program kapatılıyor...")
        break

    elif (islem == "1"):
        bilgisayar.pc_ac()

    elif (islem == "2"):
        bilgisayar.pc_kapat()

    elif (islem == "3"):
        bilgisayar.ses_ayar()

    elif (islem == "4"):
        uygulama_isimleri = input("Uygulama isimlerini ',' ile ayırarak giriniz : ")
        uygulama_listesi = uygulama_isimleri.split(",")

        for eklenecekler in uygulama_listesi:
            bilgisayar.yeni_uygulama(eklenecekler)

    elif (islem == "5"):
        silinecek_uyg = input("Silinecek uygulamaların isimlerini ',' ile ayırarak giriniz : ")
        uyg_list = silinecek_uyg.split(",")

        for silinecekler in uyg_list:
            bilgisayar.uygulama_sil(silinecekler)

    elif (islem == "6"):
        bilgisayar.rastgele_uyg()

    elif (islem == "7"):
        print("Uygulama sayısı :",len(bilgisayar))

    elif (islem == "8"):
        print(bilgisayar)

    else:
        print("Lütfen geçerli bir işlem seçiniz...")





