from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_banabiOtomatikSiparisOlustur(object):
    def setupUi(self, banabiOtomatikSiparisOlustur):
        banabiOtomatikSiparisOlustur.setObjectName("banabiOtomatikSiparisOlustur")
        banabiOtomatikSiparisOlustur.resize(600, 675)

        self.centralwidget = QtWidgets.QWidget(banabiOtomatikSiparisOlustur)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 151, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.kullaniciAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.kullaniciAdi.setGeometry(QtCore.QRect(10, 40, 281, 20))
        self.kullaniciAdi.setObjectName("kullaniciAdi")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.siparisAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.siparisAdi.setGeometry(QtCore.QRect(10, 120, 281, 20))
        self.siparisAdi.setObjectName("siparisAdi")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.parola = QtWidgets.QLineEdit(self.centralwidget)
        self.parola.setGeometry(QtCore.QRect(310, 40, 281, 20))
        self.parola.setObjectName("parola")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 90, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.sehir = QtWidgets.QLineEdit(self.centralwidget)
        self.sehir.setGeometry(QtCore.QRect(310, 120, 281, 20))
        self.sehir.setText("")
        self.sehir.setObjectName("sehir")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.birinciParca = QtWidgets.QLineEdit(self.centralwidget)
        self.birinciParca.setGeometry(QtCore.QRect(10, 200, 281, 20))
        self.birinciParca.setObjectName("birinciParca")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.ikinciParca = QtWidgets.QLineEdit(self.centralwidget)
        self.ikinciParca.setGeometry(QtCore.QRect(10, 280, 281, 20))
        self.ikinciParca.setObjectName("ikinciParca")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 330, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.ucuncuParca = QtWidgets.QLineEdit(self.centralwidget)
        self.ucuncuParca.setGeometry(QtCore.QRect(10, 360, 281, 20))
        self.ucuncuParca.setObjectName("ucuncuParca")

        self.olustur = QtWidgets.QPushButton(self.centralwidget)
        self.olustur.setGeometry(QtCore.QRect(140, 575, 321, 23))
        self.olustur.setObjectName("olustur")
        self.olustur.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.olustur.setEnabled(False)
        self.olustur.clicked.connect(self.ekle)

        self.uyari = QtWidgets.QLabel(self.centralwidget)
        self.uyari.setGeometry(QtCore.QRect(140, 600, 321, 16))
        self.uyari.setObjectName("uyari")

        self.not1 = QtWidgets.QLabel(self.centralwidget)
        self.not1.setGeometry(QtCore.QRect(140, 620, 271, 16))
        self.not1.setObjectName("not1")

        self.dorduncuParca = QtWidgets.QLineEdit(self.centralwidget)
        self.dorduncuParca.setGeometry(QtCore.QRect(10, 440, 281, 20))
        self.dorduncuParca.setObjectName("dorduncuParca")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.besinciParca = QtWidgets.QLineEdit(self.centralwidget)
        self.besinciParca.setGeometry(QtCore.QRect(10, 520, 281, 20))
        self.besinciParca.setObjectName("besinciParca")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 490, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.dorduncuParcaAdet = QtWidgets.QLineEdit(self.centralwidget)
        self.dorduncuParcaAdet.setGeometry(QtCore.QRect(310, 440, 281, 20))
        self.dorduncuParcaAdet.setObjectName("dorduncuParcaAdet")

        self.ikinciParcaAdet = QtWidgets.QLineEdit(self.centralwidget)
        self.ikinciParcaAdet.setGeometry(QtCore.QRect(310, 280, 281, 20))
        self.ikinciParcaAdet.setObjectName("ikinciParcaAdet")

        self.birinciParcaAdet = QtWidgets.QLineEdit(self.centralwidget)
        self.birinciParcaAdet.setGeometry(QtCore.QRect(310, 200, 281, 20))
        self.birinciParcaAdet.setObjectName("birinciParcaAdet")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 490, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 250, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(310, 410, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.ucuncuParcaAdet = QtWidgets.QLineEdit(self.centralwidget)
        self.ucuncuParcaAdet.setGeometry(QtCore.QRect(310, 360, 281, 20))
        self.ucuncuParcaAdet.setObjectName("ucuncuParcaAdet")

        self.besinciParcaAdet = QtWidgets.QLineEdit(self.centralwidget)
        self.besinciParcaAdet.setGeometry(QtCore.QRect(310, 520, 281, 20))
        self.besinciParcaAdet.setObjectName("besinciParcaAdet")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(310, 170, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 330, 171, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        banabiOtomatikSiparisOlustur.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(banabiOtomatikSiparisOlustur)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        banabiOtomatikSiparisOlustur.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(banabiOtomatikSiparisOlustur)
        self.statusbar.setObjectName("statusbar")

        banabiOtomatikSiparisOlustur.setStatusBar(self.statusbar)

        self.retranslateUi(banabiOtomatikSiparisOlustur)
        QtCore.QMetaObject.connectSlotsByName(banabiOtomatikSiparisOlustur)

        self.siparisAdi.textChanged.connect(self.on_text_changed)
        self.sehir.textChanged.connect(self.on_text_changed)
        self.kullaniciAdi.textChanged.connect(self.on_text_changed)
        self.parola.textChanged.connect(self.on_text_changed)
        self.birinciParca.textChanged.connect(self.on_text_changed)
        self.ikinciParca.textChanged.connect(self.on_text_changed)
        self.ucuncuParca.textChanged.connect(self.on_text_changed)
        self.dorduncuParca.textChanged.connect(self.on_text_changed)
        self.besinciParca.textChanged.connect(self.on_text_changed)
        self.birinciParcaAdet.textChanged.connect(self.on_text_changed)
        self.ikinciParcaAdet.textChanged.connect(self.on_text_changed)
        self.ucuncuParcaAdet.textChanged.connect(self.on_text_changed)
        self.dorduncuParcaAdet.textChanged.connect(self.on_text_changed)
        self.besinciParcaAdet.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        self.olustur.setEnabled(bool(self.siparisAdi.text()) and bool(self.sehir.text()) and bool(self.kullaniciAdi.text()) and bool(self.parola.text()) and bool(self.birinciParca.text()) and bool(self.birinciParcaAdet.text()) and bool(self.ikinciParca.text()) and bool(self.ikinciParcaAdet.text()) and bool(self.ucuncuParca.text()) and bool(self.ucuncuParcaAdet.text()) and bool(self.dorduncuParca.text()) and bool(self.dorduncuParcaAdet.text()) and bool(self.besinciParca.text()) and bool(self.besinciParcaAdet.text()))
    

    def retranslateUi(self, banabiOtomatikSiparisOlustur):
        _translate = QtCore.QCoreApplication.translate
        banabiOtomatikSiparisOlustur.setWindowTitle(_translate("banabiOtomatikSiparisOlustur", "Otomatik Sipariş Oluştur"))
        self.label.setText(_translate("banabiOtomatikSiparisOlustur", "Siparişinizi isimlendirin: "))
        self.label_2.setText(_translate("banabiOtomatikSiparisOlustur", "Yemeksepeti Kullanıcı Adı:"))
        self.label_3.setText(_translate("banabiOtomatikSiparisOlustur", "Yemeksepeti Parola:"))
        self.label_4.setText(_translate("banabiOtomatikSiparisOlustur", "Şehir:"))
        self.label_5.setText(_translate("banabiOtomatikSiparisOlustur", "Birinci Parça:"))
        self.label_6.setText(_translate("banabiOtomatikSiparisOlustur", "İkinci Parça:"))
        self.label_7.setText(_translate("banabiOtomatikSiparisOlustur", "Üçüncü Parça:"))
        self.olustur.setText(_translate("banabiOtomatikSiparisOlustur", "Oluştur"))
        self.uyari.setText(_translate("banabiOtomatikSiparisOlustur", "Uyarı: Girdiğiniz parça isimleri Banabi\'dekiler ile birebir aynı olmalıdır."))
        self.not1.setText(_translate("banabiOtomatikSiparisOlustur", "Not: Sipariş etmek istemediğiniz parçalara \'Hayır\' yazınız."))
        self.label_10.setText(_translate("banabiOtomatikSiparisOlustur", "Dördüncü Parça:"))
        self.label_11.setText(_translate("banabiOtomatikSiparisOlustur", "Beşinci Parça:"))
        self.label_12.setText(_translate("banabiOtomatikSiparisOlustur", "Beşinci Parça Adet:"))
        self.label_13.setText(_translate("banabiOtomatikSiparisOlustur", "İkinci Parça Adet:"))
        self.label_14.setText(_translate("banabiOtomatikSiparisOlustur", "Dörüncü Parça Adet:"))
        self.label_15.setText(_translate("banabiOtomatikSiparisOlustur", "Birinci Parça Adet:"))
        self.label_16.setText(_translate("banabiOtomatikSiparisOlustur", "Üçüncü Parça Adet:"))

    def tabloOlustur():
        con = sqlite3.connect("otomatikSiparisler.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS BanabiOtomatikSiparisler (Siparis_Adi TEXT, Sehir TEXT, Kullanici_Adi TEXT, Parola TEXT, Birinci_Parca TEXT, Birinci_Parca_Adet INT, İkinci_Parca TEXT, İkinci_Parca_Adet INT, Ucuncu_Parca TEXT, Ucuncu_Parca_Adet INT, Dorduncu_Parca TEXT, Dorduncu_Parca_Adet INT, Besinci_Parca TEXT, Besinci_Parca_Adet INT)")
        con.commit()

    tabloOlustur()

    def ekle(self):
        con = sqlite3.connect("otomatikSiparisler.db")
        cursor = con.cursor()

        siparisAdiDonut = self.siparisAdi.text()
        cursor.execute("Select * From BanabiOtomatikSiparisler[0]")
        veri = cursor.fetchall()

        try:
            siparisAdlari = []
            cursor.execute("Select Siparis_Adi from BanabiOtomatikSiparisler")
            veri = cursor.fetchall()

            Siparis1 = None
            Siparis2 = None
            Siparis3 = None
            Siparis4 = None
            Siparis5 = None
            Siparis6 = None
            Siparis7 = None
            Siparis8 = None
            Siparis9 = None

            def convertTuple(tup): 
                str =  ''.join(tup) 
                return str

            for i in veri:  
                i = convertTuple(i)
                siparisAdlari.append(i)

            if (len(siparisAdlari) == 1):
                Siparis1 = str(siparisAdlari[0])

            elif (len(siparisAdlari) == 2):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])

            elif (len(siparisAdlari) == 3):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])

            elif (len(siparisAdlari) == 4):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])

            elif (len(siparisAdlari) == 5):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])
                Siparis5 = str(siparisAdlari[4])

            elif (len(siparisAdlari) == 6):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])
                Siparis5 = str(siparisAdlari[4])
                Siparis6 = str(siparisAdlari[5])

            elif (len(siparisAdlari) == 7):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])
                Siparis5 = str(siparisAdlari[4])
                Siparis6 = str(siparisAdlari[5])
                Siparis7 = str(siparisAdlari[6])

            elif (len(siparisAdlari) == 8):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])
                Siparis5 = str(siparisAdlari[4])
                Siparis6 = str(siparisAdlari[5])
                Siparis7 = str(siparisAdlari[6])
                Siparis8 = str(siparisAdlari[7])

            elif (len(siparisAdlari) == 9):
                Siparis1 = str(siparisAdlari[0])
                Siparis2 = str(siparisAdlari[1])
                Siparis3 = str(siparisAdlari[2])
                Siparis4 = str(siparisAdlari[3])
                Siparis5 = str(siparisAdlari[4])
                Siparis6 = str(siparisAdlari[5])
                Siparis7 = str(siparisAdlari[6])
                Siparis8 = str(siparisAdlari[7])
                Siparis9 = str(siparisAdlari[8])

            if len(veri) < 10:

                if (siparisAdiDonut == Siparis1) or (siparisAdiDonut == Siparis2) or (siparisAdiDonut == Siparis3) or (siparisAdiDonut == Siparis4) or (siparisAdiDonut == Siparis5) or (siparisAdiDonut == Siparis6) or (siparisAdiDonut == Siparis7) or (siparisAdiDonut == Siparis8) or (siparisAdiDonut == Siparis9):

                    def popUp3(self):
                        msg = QMessageBox()
                        msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                        msg.setText("Girmiş olduğunuz isim ile başka bir otomatik sipariş bulunuyor, lütfen farklı bir isim ile yeniden deneyiniz.")
                        msg.setIcon(QMessageBox.Warning)

                        x = msg.exec()
                
                    popUp3(self)

                else:

                    def tabloOlustur():
                        cursor.execute("CREATE TABLE IF NOT EXISTS BanabiOtomatikSiparisler (Siparis_Adi TEXT, Sehir TEXT, Kullanici_Adi TEXT, Parola TEXT, Birinci_Parca TEXT, Birinci_Parca_Adet INT, İkinci_Parca TEXT, İkinci_Parca_Adet INT, Ucuncu_Parca TEXT, Ucuncu_Parca_Adet INT, Dorduncu_Parca TEXT, Dorduncu_Parca_Adet INT, Besinci_Parca TEXT, Besinci_Parca_Adet INT)")
                        con.commit()

                    def bilgileriAktar():
                        siparisAdiDonut = self.siparisAdi.text()
                        sehirDonut = self.sehir.text()
                        kullanciAdiDonut = self.kullaniciAdi.text()
                        parolaDonut = self.parola.text()
                        birinciParcaDonut = self.birinciParca.text()
                        birinciParcaAdetDonut = self.birinciParcaAdet.text()
                        ikinciParcaDonut = self.ikinciParca.text()
                        ikinciParcaAdetDonut = self.ikinciParcaAdet.text()
                        ucuncuParcaDonut = self.ucuncuParca.text()
                        ucuncuParcaAdetDonut = self.ucuncuParcaAdet.text()
                        dorduncuParcaDonut = self.dorduncuParca.text()
                        dorduncuParcaAdetDonut = self.dorduncuParcaAdet.text()
                        besinciParcaDonut = self.besinciParca.text()
                        besinciParcaAdetDonut = self.besinciParcaAdet.text()

                        cursor.execute("INSERT INTO BanabiOtomatikSiparisler VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (siparisAdiDonut, sehirDonut, kullanciAdiDonut, parolaDonut, birinciParcaDonut, birinciParcaAdetDonut, ikinciParcaDonut, ikinciParcaAdetDonut, ucuncuParcaDonut, ucuncuParcaAdetDonut, dorduncuParcaDonut, dorduncuParcaAdetDonut, besinciParcaDonut, besinciParcaAdetDonut))
                        con.commit()


                    def popUp1(self):
                        msg = QMessageBox()
                        msg.setWindowTitle("Otomatik Sipariş Oluşturuldu")
                        msg.setText("Sağladığınız bilgiler doğrultusunda yeni bir otomatik sipariş oluşturdunuz.")
                        msg.setIcon(QMessageBox.Information)

                        x = msg.exec()

                    tabloOlustur()
                    bilgileriAktar()
                    popUp1(self)
                    con.close()

            else:
                def popUp2(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                    msg.setText("Halihazırda on adet otomatik siparişiniz bulunduğu için yeni bir otomatik sipariş oluşturamazsınız.")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                
                popUp2(self)


        except IndexError:

            if len(veri) < 10:

                def tabloOlustur():
                        cursor.execute("CREATE TABLE IF NOT EXISTS BanabiOtomatikSiparisler (Siparis_Adi TEXT, Sehir TEXT, Kullanici_Adi TEXT, Parola TEXT, Birinci_Parca TEXT, Birinci_Parca_Adet INT, İkinci_Parca TEXT, İkinci_Parca_Adet INT, Ucuncu_Parca TEXT, Ucuncu_Parca_Adet INT, Dorduncu_Parca TEXT, Dorduncu_Parca_Adet INT, Besinci_Parca TEXT, Besinci_Parca_Adet INT)")
                        con.commit()

                def bilgileriAktar():
                    siparisAdiDonut = self.siparisAdi.text()
                    sehirDonut = self.sehir.text()
                    kullanciAdiDonut = self.kullaniciAdi.text()
                    parolaDonut = self.parola.text()
                    birinciParcaDonut = self.birinciParca.text()
                    birinciParcaAdetDonut = self.birinciParcaAdet.text()
                    ikinciParcaDonut = self.ikinciParca.text()
                    ikinciParcaAdetDonut = self.ikinciParcaAdet.text()
                    ucuncuParcaDonut = self.ucuncuParca.text()
                    ucuncuParcaAdetDonut = self.ucuncuParcaAdet.text()
                    dorduncuParcaDonut = self.dorduncuParca.text()
                    dorduncuParcaAdetDonut = self.dorduncuParcaAdet.text()
                    besinciParcaDonut = self.besinciParca.text()
                    besinciParcaAdetDonut = self.besinciParcaAdet.text()

                    cursor.execute("INSERT INTO BanabiOtomatikSiparisler VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (siparisAdiDonut, sehirDonut, kullanciAdiDonut, parolaDonut, birinciParcaDonut, birinciParcaAdetDonut, ikinciParcaDonut, ikinciParcaAdetDonut, ucuncuParcaDonut, ucuncuParcaAdetDonut, dorduncuParcaDonut, dorduncuParcaAdetDonut, besinciParcaDonut, besinciParcaAdetDonut))
                    con.commit()

                def popUp1(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturuldu")
                    msg.setText("Sağladığınız bilgiler doğrultusunda yeni bir otomatik sipariş oluşturdunuz.")
                    msg.setIcon(QMessageBox.Information)

                    x = msg.exec()

                tabloOlustur()
                bilgileriAktar()
                popUp1(self)
                con.close()

            else:
                def popUp2(self):
                    msg = QMessageBox()
                    msg.setWindowTitle("Otomatik Sipariş Oluşturulamadı")
                    msg.setText("Halihazırda on adet otomatik siparişiniz bulunduğu için yeni bir otomatik sipariş oluşturamazsınız.")
                    msg.setIcon(QMessageBox.Warning)

                    x = msg.exec()
                
                popUp2(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banabiOtomatikSiparisOlustur = QtWidgets.QMainWindow()
    ui = Ui_banabiOtomatikSiparisOlustur()
    ui.setupUi(banabiOtomatikSiparisOlustur)
    banabiOtomatikSiparisOlustur.show()
    sys.exit(app.exec_())
