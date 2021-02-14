import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists Üyeler (kullanici_adi TEXT,parola TEXT)")

        self.baglanti.commit()


    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        self.uye_ol = QtWidgets.QPushButton("Üye Ol")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.uye_ol)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")

        self.giris.clicked.connect(self.login)

        self.uye_ol.clicked.connect(self.register)

        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("SELECT * FROM Üyeler WHERE kullanici_adi = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)

    def register(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * FROM Üyeler WHERE kullanici_adi = ?",(adi,))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.cursor.execute("Insert into Üyeler VALUES(?,?)",(adi,par))
            self.yazi_alani.setText("Kayıt başarıyla gerçekleştirildi.")
            self.baglanti.commit()
        else:
            self.yazi_alani.setText("Kullanıcı adı alınmış.\nLütfen başka bir kullanıcı adı deneyiniz.")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

