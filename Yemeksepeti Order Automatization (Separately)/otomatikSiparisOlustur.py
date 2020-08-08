from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_otomatikSiparisOlustur(object):
    def setupUi(self, otomatikSiparisOlustur):
        otomatikSiparisOlustur.setObjectName("otomatikSiparisOlustur")
        otomatikSiparisOlustur.resize(600, 700)

        self.centralwidget = QtWidgets.QWidget(otomatikSiparisOlustur)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 160, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.siparisAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.siparisAdi.setGeometry(QtCore.QRect(140, 40, 281, 20))
        self.siparisAdi.setObjectName("siparisAdi")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.kullaniciAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.kullaniciAdi.setGeometry(QtCore.QRect(140, 110, 281, 20))
        self.kullaniciAdi.setObjectName("kullaniciAdi")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.parola = QtWidgets.QLineEdit(self.centralwidget)
        self.parola.setGeometry(QtCore.QRect(140, 180, 281, 20))
        self.parola.setObjectName("parola")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)

        self.sehirl = QtWidgets.QLabel(self.centralwidget)
        self.sehirl.setGeometry(QtCore.QRect(140, 220, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.sehirl.setFont(font)
        self.sehirl.setObjectName("sehirl")

        self.sehir = QtWidgets.QLineEdit(self.centralwidget)
        self.sehir.setGeometry(QtCore.QRect(140, 250, 281, 20))
        self.sehir.setObjectName("sehir")

        self.restoranl = QtWidgets.QLabel(self.centralwidget)
        self.restoranl.setGeometry(QtCore.QRect(140, 290, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.restoranl.setFont(font)
        self.restoranl.setObjectName("restoranl")

        self.restoran = QtWidgets.QLineEdit(self.centralwidget)
        self.restoran.setGeometry(140, 320, 281, 20)
        self.restoran.setObjectName("restoran")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 360, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.birinciParca = QtWidgets.QLineEdit(self.centralwidget)
        self.birinciParca.setGeometry(QtCore.QRect(140, 390, 281, 20))
        self.birinciParca.setObjectName("birinciParca")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 430, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.ikinciParca = QtWidgets.QLineEdit(self.centralwidget)
        self.ikinciParca.setGeometry(QtCore.QRect(140, 460, 281, 20))
        self.ikinciParca.setObjectName("ikinciParca")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 500, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.ucuncuParca = QtWidgets.QLineEdit(self.centralwidget)
        self.ucuncuParca.setGeometry(QtCore.QRect(140, 530, 281, 20))
        self.ucuncuParca.setObjectName("ucuncuParca")

        self.olustur = QtWidgets.QPushButton(self.centralwidget)
        self.olustur.setGeometry(QtCore.QRect(140, 570, 281, 23))
        self.olustur.setObjectName("olustur")
        self.olustur.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.olustur.setEnabled(False)

        self.olustur.clicked.connect(self.ekle)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 620, 361, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 640, 361, 16))
        self.label_9.setObjectName("label_9")

        otomatikSiparisOlustur.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(otomatikSiparisOlustur)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        otomatikSiparisOlustur.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(otomatikSiparisOlustur)
        self.statusbar.setObjectName("statusbar")

        otomatikSiparisOlustur.setStatusBar(self.statusbar)

        self.retranslateUi(otomatikSiparisOlustur)
        QtCore.QMetaObject.connectSlotsByName(otomatikSiparisOlustur)

        self.siparisAdi.textChanged.connect(self.on_text_changed)
        self.kullaniciAdi.textChanged.connect(self.on_text_changed)
        self.parola.textChanged.connect(self.on_text_changed)
        self.restoran.textChanged.connect(self.on_text_changed)
        self.birinciParca.textChanged.connect(self.on_text_changed)
        self.ikinciParca.textChanged.connect(self.on_text_changed)
        self.ucuncuParca.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        self.olustur.setEnabled(bool(self.siparisAdi.text()) and bool(self.kullaniciAdi.text()) and bool(self.parola.text()) and bool(self.restoran.text()) and bool(self.birinciParca.text()) and bool(self.ikinciParca.text()) and bool(self.ucuncuParca.text()))


    def retranslateUi(self, otomatikSiparisOlustur):
        _translate = QtCore.QCoreApplication.translate
        otomatikSiparisOlustur.setWindowTitle(_translate("otomatikSiparisOlustur", "Otomatik Sipariş Oluştur"))
        self.label.setText(_translate("otomatikSiparisOlustur", "Siparişinizi isimlendirin: "))
        self.label_2.setText(_translate("otomatikSiparisOlustur", "Yemeksepeti Kullanıcı Adı:"))
        self.label_3.setText(_translate("otomatikSiparisOlustur", "Yemeksepeti Parola:"))
        self.sehirl.setText(_translate("otomatikSiparisOlustur", "Şehir:"))
        self.restoranl.setText(_translate("otomatikSiparisOlustur", "Restoran:"))
        self.label_5.setText(_translate("otomatikSiparisOlustur", "Birinci Parça:"))
        self.label_6.setText(_translate("otomatikSiparisOlustur", "İkinci Parça:"))
        self.label_7.setText(_translate("otomatikSiparisOlustur", "Üçüncü Parça:"))
        self.olustur.setText(_translate("otomatikSiparisOlustur", "Oluştur"))
        self.label_8.setText(_translate("otomatikSiparisOlustur", "Uyarı: Girdiğiniz parça isimleri Yemeksepeti\'ndekiler ile birebir aynı olmalıdır."))
        self.label_9.setText(_translate("otomatikSiparisOlustur", "Not: Sipariş etmek istemediğiniz kısımlara 'Hayır' yazınız."))

    def tabloOlustur():
        con = sqlite3.connect("otomatikMenuler.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS OtomatikSiparisler (Siparis_Adi TEXT, Kullanici_Adi TEXT, Parola TEXT, Sehir TEXT, Restoran TEXT, Birinci_Parca TEXT, Ikinci_Parca TEXT, Ucuncu_Parca TEXT)")
        con.commit()
    
    tabloOlustur()

    def ekle(self):
        con = sqlite3.connect("otomatikMenuler.db")
        cursor = con.cursor()

        siparisAdiDonut = self.siparisAdi.text()
        cursor.execute("Select * From OtomatikSiparisler[0]")
        veri = cursor.fetchall()
        
        try:

            siparisAdlari = []
            cursor.execute("Select Siparis_Adi From OtomatikSiparisler")
            veri = cursor.fetchall()

            Menu1 = None
            Menu2 = None
            Menu3 = None
            Menu4 = None

            def convertTuple(tup): 
                str =  ''.join(tup) 
                return str

            for i in veri:  
                i = convertTuple(i)
                siparisAdlari.append(i)

            if (len(siparisAdlari) == 1):

                Menu1 = str(siparisAdlari[0])

            elif (len(siparisAdlari) == 2):

                Menu1 = str(siparisAdlari[0])
                Menu2 = str(siparisAdlari[1])

            elif (len(siparisAdlari) == 3):

                Menu1 = str(siparisAdlari[0])
                Menu2 = str(siparisAdlari[1])
                Menu3 = str(siparisAdlari[2])

            elif (len(siparisAdlari) == 4):

                Menu1 = str(siparisAdlari[0])
                Menu2 = str(siparisAdlari[1])
                Menu3 = str(siparisAdlari[2])
                Menu4 = str(siparisAdlari[3])

            if (len(veri) < 5):

                if (siparisAdiDonut == Menu1) or  (siparisAdiDonut == Menu2) or  (siparisAdiDonut == Menu3) or (siparisAdiDonut == Menu4):

                    def popUp3(self):
                        msg = QMessageBox()
                        msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                        msg.setText("Girmiş olduğunuz isim ile başka bir otomatik sipariş bulunuyor, lütfen farklı bir isim ile yeniden deneyiniz.")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                
                    popUp3(self)
                
                else:

                    def tabloOlustur():
                        cursor.execute("CREATE TABLE IF NOT EXISTS OtomatikSiparisler (Siparis_Adi TEXT, Kullanici_Adi TEXT, Parola TEXT, Sehir TEXT, Restoran TEXT, Birinci_Parca TEXT, Ikinci_Parca TEXT, Ucuncu_Parca TEXT)")
                        con.commit()

                    def bilgileriAktar():
                        kullaniciAdiDonut = self.kullaniciAdi.text()
                        parolaDonut = self.parola.text()
                        sehirDonut = self.sehir.text()
                        restoranDonut = self.restoran.text()
                        birinciParcaDonut = self.birinciParca.text()
                        ikinciParcaDonut = self.ikinciParca.text()
                        ucuncuParcaDonut = self.ucuncuParca.text()
                        siparisAdiDonut = self.siparisAdi.text()

                        cursor.execute("INSERT INTO OtomatikSiparisler VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(siparisAdiDonut, kullaniciAdiDonut, parolaDonut, sehirDonut, restoranDonut, birinciParcaDonut, ikinciParcaDonut, ucuncuParcaDonut))            
                        con.commit()

                    def popUp1(self):
                        msg = QMessageBox()
                        msg.setWindowTitle("Otomatik Sipariş Oluşturuldu")
                        msg.setText("Sağladığınız bilgiler doğrultusunda yeni bir otomatik sipariş oluşturdunuz.")
                        msg.setIcon(QMessageBox.Information)
                
                
                    tabloOlustur()
                    bilgileriAktar()
                    popUp1(self)
                    con.close()

            else:
                def popUp2(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                    msg.setText("Halihazırda beş adet otomatik siparişiniz bulunduğu için yeni bir otomatik sipariş oluşturamazsınız.")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                
                popUp2(self)

        except IndexError:

            if (len(veri) < 5):
                def tabloOlustur():
                        cursor.execute("CREATE TABLE IF NOT EXISTS OtomatikSiparisler (Siparis_Adi TEXT, Kullanici_Adi TEXT, Parola TEXT, Sehir TEXT, Restoran TEXT, Birinci_Parca TEXT, Ikinci_Parca TEXT, Ucuncu_Parca TEXT)")
                        con.commit()

                def bilgileriAktar():
                    kullaniciAdiDonut = self.kullaniciAdi.text()
                    parolaDonut = self.parola.text()
                    sehirDonut = self.sehir.text()
                    restoranDonut = self.restoran.text()
                    birinciParcaDonut = self.birinciParca.text()
                    ikinciParcaDonut = self.ikinciParca.text()
                    ucuncuParcaDonut = self.ucuncuParca.text()
                    siparisAdiDonut = self.siparisAdi.text()

                    cursor.execute("INSERT INTO OtomatikSiparisler VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(siparisAdiDonut, kullaniciAdiDonut, parolaDonut, sehirDonut, restoranDonut, birinciParcaDonut, ikinciParcaDonut, ucuncuParcaDonut))            
                    con.commit()

                def popUp1(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturuldu")
                    msg.setText("Sağladığınız bilgiler doğrultusunda yeni bir otomatik sipariş oluşturdunuz.")
                    msg.setIcon(QMessageBox.Information)
                
                
                tabloOlustur()
                bilgileriAktar()
                popUp1(self)
                con.close()

            else:
                def popUp2(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                    msg.setText("Halihazırda beş adet otomatik siparişiniz bulunduğu için yeni bir otomatik sipariş oluşturamazsınız.")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                
                popUp2(self)


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otomatikSiparisOlustur = QtWidgets.QMainWindow()
    ui = Ui_otomatikSiparisOlustur()
    ui.setupUi(otomatikSiparisOlustur)
    otomatikSiparisOlustur.show()
    sys.exit(app.exec_())
