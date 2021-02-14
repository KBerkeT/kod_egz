import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, QtGui, QtWidgets

class Mail(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.mesaj_from = QtWidgets.QLineEdit()
        self.mesaj_to = QtWidgets.QLineEdit()
        self.mesaj_subject = QtWidgets.QLineEdit()
        self.mesaj = QtWidgets.QTextEdit()
        self.from_lable = QtWidgets.QLabel("E-mail  : ")
        self.to_lable = QtWidgets.QLabel("To     : ")
        self.subject_lable = QtWidgets.QLabel("Subject : ")
        self.mesajı_temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Dosya Aç")
        self.gonder = QtWidgets.QPushButton("Gönder")
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola_lable = QtWidgets.QLabel("Parola : ")
        self.yazi_alani = QtWidgets.QLabel("")


        h_box1 = QtWidgets.QHBoxLayout()

        h_box1.addWidget(self.from_lable)
        h_box1.addWidget(self.mesaj_from)


        h_box1_2 = QtWidgets.QHBoxLayout()

        h_box1_2.addWidget(self.parola_lable)
        h_box1_2.addWidget(self.parola)


        h_box2 = QtWidgets.QHBoxLayout()

        h_box2.addWidget(self.to_lable)
        h_box2.addWidget(self.mesaj_to)


        h_box3 = QtWidgets.QHBoxLayout()

        h_box3.addWidget(self.mesajı_temizle)
        h_box3.addWidget(self.ac)
        h_box3.addWidget(self.gonder)


        h_box4 = QtWidgets.QHBoxLayout()

        h_box4.addWidget(self.subject_lable)
        h_box4.addWidget(self.mesaj_subject)


        v_box = QtWidgets.QVBoxLayout()

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box1_2)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.mesaj)
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box3)


        self.setLayout(v_box)

        self.setWindowTitle("Mail Gönderme")

        self.mesajı_temizle.clicked.connect(self.hepsini_sil)
        self.ac.clicked.connect(self.dosya_ac)
        self.gonder.clicked.connect(self.mail_gonder)

        self.show()

    def hepsini_sil(self):
        self.mesaj.clear()
    def dosya_ac(self):
        dosya_ismi = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:
            self.mesaj.setText(file.read())

    def mail_gonder(self):

        mesaj = MIMEMultipart()

        mesaj["From"] = self.mesaj_from.text()

        mesaj["To"] = self.mesaj_to.text()

        mesaj["subject"] = self.mesaj_subject.text()

        yazi = self.mesaj.toPlainText()

        mesaj_govdesi = MIMEText(yazi,"plain")

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)

            mail.starttls()

            mail.login(self.mesaj_from.text(),self.parola.text())

            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

            print("Mail başarıyla gçnderildi...")

            mail.close()

        except:
            sys.stderr.write("Bir sorun oluştu!!!\nLütfen tekrar deneyiniz...")
            sys.stderr.flush()



app = QtWidgets.QApplication(sys.argv)

mail = Mail()

sys.exit(app.exec_())