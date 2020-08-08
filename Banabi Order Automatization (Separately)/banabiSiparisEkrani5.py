from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sqlite3

con = sqlite3.connect("otomatikSiparisler.db")
cursor = con.cursor()

class Ui_banabiSiparisEkrani5(object):
    def setupUi(self, banabiSiparisEkrani5):

        banabiSiparisEkrani5.setObjectName("banabiSiparisEkrani5")
        banabiSiparisEkrani5.resize(500, 675)

        self.centralwidget = QtWidgets.QWidget(banabiSiparisEkrani5)
        self.centralwidget.setObjectName("centralwidget")

        self.siparisAdi = QtWidgets.QLabel(self.centralwidget)
        self.siparisAdi.setGeometry(QtCore.QRect(20, 20, 381, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.siparisAdi.setFont(font)
        self.siparisAdi.setObjectName("siparisAdi")

        self.kullaniciAdi = QtWidgets.QLabel(self.centralwidget)
        self.kullaniciAdi.setGeometry(QtCore.QRect(20, 120, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.kullaniciAdi.setFont(font)
        self.kullaniciAdi.setObjectName("kullaniciAdi")

        self.sehir = QtWidgets.QLabel(self.centralwidget)
        self.sehir.setGeometry(QtCore.QRect(20, 70, 391, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.sehir.setFont(font)
        self.sehir.setObjectName("sehir")

        self.birinciParca = QtWidgets.QLabel(self.centralwidget)
        self.birinciParca.setGeometry(QtCore.QRect(20, 170, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.birinciParca.setFont(font)
        self.birinciParca.setObjectName("birinciParca")

        self.siparisiSil = QtWidgets.QPushButton(self.centralwidget)
        self.siparisiSil.setGeometry(QtCore.QRect(270, 600, 181, 41))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)

        self.siparisiSil.setFont(font)
        self.siparisiSil.setStyleSheet("background-color: rgb(255, 0, 0); border: none; color: rgb(0, 0, 0);")
        self.siparisiSil.setObjectName("siparisiSil")
        self.siparisiSil.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparisiSil.clicked.connect(self.siparisiSilme)

        self.siparisVer = QtWidgets.QPushButton(self.centralwidget)
        self.siparisVer.setGeometry(QtCore.QRect(20, 600, 181, 41))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.siparisVer.setFont(font)
        self.siparisVer.setStyleSheet("background-color: rgb(0, 255, 0); border: none; color: rgb(0, 0, 0);")
        self.siparisVer.setObjectName("siparisVer")
        self.siparisVer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparisVer.clicked.connect(self.siparisVerme)

        self.birinciParcaAdet = QtWidgets.QLabel(self.centralwidget)
        self.birinciParcaAdet.setGeometry(QtCore.QRect(20, 200, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.birinciParcaAdet.setFont(font)
        self.birinciParcaAdet.setObjectName("label_9")

        self.ikinciParca = QtWidgets.QLabel(self.centralwidget)
        self.ikinciParca.setGeometry(QtCore.QRect(20, 250, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ikinciParca.setFont(font)
        self.ikinciParca.setObjectName("label_7")

        self.ikinciParcaAdet = QtWidgets.QLabel(self.centralwidget)
        self.ikinciParcaAdet.setGeometry(QtCore.QRect(20, 280, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ikinciParcaAdet.setFont(font)
        self.ikinciParcaAdet.setObjectName("ikinciParcaAdet")

        self.ucuncuParca = QtWidgets.QLabel(self.centralwidget)
        self.ucuncuParca.setGeometry(QtCore.QRect(20, 330, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ucuncuParca.setFont(font)
        self.ucuncuParca.setObjectName("ucuncuParca")

        self.ucuncuParcaAdet = QtWidgets.QLabel(self.centralwidget)
        self.ucuncuParcaAdet.setGeometry(QtCore.QRect(20, 360, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ucuncuParcaAdet.setFont(font)
        self.ucuncuParcaAdet.setObjectName("ucuncuParcaAdet")

        self.dorduncuParcaAdet = QtWidgets.QLabel(self.centralwidget)
        self.dorduncuParcaAdet.setGeometry(QtCore.QRect(20, 440, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.dorduncuParcaAdet.setFont(font)
        self.dorduncuParcaAdet.setObjectName("dorduncuParcaAdet")

        self.dorduncuParca = QtWidgets.QLabel(self.centralwidget)
        self.dorduncuParca.setGeometry(QtCore.QRect(20, 410, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.dorduncuParca.setFont(font)
        self.dorduncuParca.setObjectName("dorduncuParca")

        self.besinciParca = QtWidgets.QLabel(self.centralwidget)
        self.besinciParca.setGeometry(QtCore.QRect(20, 490, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.besinciParca.setFont(font)
        self.besinciParca.setObjectName("besinciParca")

        self.besinciParcaAdet = QtWidgets.QLabel(self.centralwidget)
        self.besinciParcaAdet.setGeometry(QtCore.QRect(20, 520, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.besinciParcaAdet.setFont(font)
        self.besinciParcaAdet.setObjectName("besinciParcaAdet")

        banabiSiparisEkrani5.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(banabiSiparisEkrani5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")

        banabiSiparisEkrani5.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(banabiSiparisEkrani5)
        self.statusbar.setObjectName("statusbar")

        banabiSiparisEkrani5.setStatusBar(self.statusbar)

        self.retranslateUi(banabiSiparisEkrani5)
        QtCore.QMetaObject.connectSlotsByName(banabiSiparisEkrani5)

    def retranslateUi(self, banabiSiparisEkrani5):
        cursor.execute("Select * From BanabiOtomatikSiparisler[0]")
        veri = cursor.fetchall()

        try:
            bilgiler = veri[4]
            siparisAdi = bilgiler[0]
            sehir = bilgiler[1]
            kullaniciAdi = bilgiler[2]
            birinciParca = bilgiler [4]
            birinciParcaAdet = bilgiler [5]
            ikinciParca = bilgiler[6]
            ikinciParcaAdet = bilgiler[7]
            ucuncuParca = bilgiler[8]
            ucuncuParcaAdet = bilgiler[9]
            dorduncuParca = bilgiler[10]
            dorduncuParcaAdet = bilgiler[11]
            besinciParca = bilgiler[12]
            besinciParcaAdet = bilgiler[13]

            _translate = QtCore.QCoreApplication.translate
            banabiSiparisEkrani5.setWindowTitle(_translate("banabiSiparisEkrani5", siparisAdi))

            self.siparisAdi.setText(_translate("banabiSiparisEkrani5", "Sipariş Adı:  "+siparisAdi))
            self.kullaniciAdi.setText(_translate("banabiSiparisEkrani5", "Yemeksepeti Hesabı:  "+kullaniciAdi))
            self.sehir.setText(_translate("banabiSiparisEkrani5", "Şehir:  "+sehir))
            self.birinciParca.setText(_translate("banabiSiparisEkrani5", "Birinci Parça:  "+birinciParca))
            self.birinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "Birinci Parça Adet:  "+str(birinciParcaAdet)))
            self.ikinciParca.setText(_translate("banabiSiparisEkrani5", "İkinci Parça:  "+ikinciParca))
            self.ikinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "İkinci Parça Adet:  "+str(ikinciParcaAdet)))
            self.ucuncuParca.setText(_translate("banabiSiparisEkrani5", "Üçüncü Parça:  "+ucuncuParca))
            self.ucuncuParcaAdet.setText(_translate("banabiSiparisEkrani5", "Üçüncü Parça Adet:  "+str(ucuncuParcaAdet)))
            self.dorduncuParca.setText(_translate("banabiSiparisEkrani5", "Dördüncü Parça:  "+dorduncuParca))
            self.dorduncuParcaAdet.setText(_translate("banabiSiparisEkrani5", "Dördüncü Parça Adet:  "+str(dorduncuParcaAdet)))
            self.besinciParca.setText(_translate("banabiSiparisEkrani5", "Beşinci Parça:  "+besinciParca))
            self.besinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "Beşinci Parça Adet:  "+str(besinciParcaAdet)))
            self.siparisiSil.setText(_translate("banabiSiparisEkrani5", "Siparişi Sil"))
            self.siparisVer.setText(_translate("banabiSiparisEkrani5", "Sipariş Ver"))
        
        except IndexError:
            siparisAdi = "Boş"
            kullaniciAdi = "Boş"
            sehir = "Boş"
            restoran = "Boş"
            birinciParca = "Boş"
            birinciParcaAdet = "0"
            ikinciParca = "Boş"
            ikinciParcaAdet = "0"
            ucuncuParca = "Boş"
            ucuncuParcaAdet = "0"
            dorduncuParca = "Boş"
            dorduncuParcaAdet = "0"
            besinciParca = "Boş"
            besinciParcaAdet = "0"

            _translate = QtCore.QCoreApplication.translate
            banabiSiparisEkrani5.setWindowTitle(_translate("banabiSiparisEkrani5", "Boş Menü"))

            self.siparisAdi.setText(_translate("banabiSiparisEkrani5", "Sipariş Adı:  "+siparisAdi))
            self.kullaniciAdi.setText(_translate("banabiSiparisEkrani5", "Yemeksepeti Hesabı:  "+kullaniciAdi))
            self.sehir.setText(_translate("banabiSiparisEkrani5", "Şehir:  "+sehir))
            self.birinciParca.setText(_translate("banabiSiparisEkrani5", "Birinci Parça:  "+birinciParca))
            self.birinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "Birinci Parça Adet:  "+birinciParcaAdet))
            self.ikinciParca.setText(_translate("banabiSiparisEkrani5", "İkinci Parça:  "+ikinciParca))
            self.ikinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "İkinci Parça Adet:  "+ikinciParcaAdet))
            self.ucuncuParca.setText(_translate("banabiSiparisEkrani5", "Üçüncü Parça:  "+ucuncuParca))
            self.ucuncuParcaAdet.setText(_translate("banabiSiparisEkrani5", "Üçüncü Parça Adet:  "+ucuncuParcaAdet))
            self.dorduncuParca.setText(_translate("banabiSiparisEkrani5", "Dördün Parça:  "+dorduncuParca))
            self.dorduncuParcaAdet.setText(_translate("banabiSiparisEkrani5", "Dördüncü Parça Adet:  "+dorduncuParcaAdet))
            self.besinciParca.setText(_translate("banabiSiparisEkrani5", "Beşinci Parça:  "+besinciParca))
            self.besinciParcaAdet.setText(_translate("banabiSiparisEkrani5", "Beşinci Parça Adet:  "+besinciParcaAdet))
            self.siparisiSil.setText(_translate("banabiSiparisEkrani5", "Siparişi Sil"))
            self.siparisVer.setText(_translate("banabiSiparisEkrani5", "Sipariş Ver"))

    def siparisiSilme(self):
        def popUp1(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Silindi")
            msg.setText("Seçmiş olduğunuz sipariş silindi.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec()
        def popUp2(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Boş")
            msg.setText("Seçmiş olduğunuz sipariş boş olduğu için silinemiyor.")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec()
        try:
            cursor.execute("Select * From BanabiOtomatikSiparisler[0]")
            veri = cursor.fetchall()
            bilgiler = veri[4]
            siparisAdi = bilgiler[0]
            cursor.execute("Delete From BanabiOtomatikSiparisler where Siparis_Adi = ?", (siparisAdi,))
            con.commit()
            popUp1(self)
        except IndexError:
            popUp2(self)

    def siparisVerme(self):
        def popUp3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Verildi")
            msg.setText("Seçmiş olduğunuz otomatik sipariş sepetinize eklendi.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec()

        def popUp4(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Verilemedi")
            msg.setText("Seçmiş olduğunuz sipariş boş, lütfen yeni bir sipariş oluşturun ya da var olan bir sipariş verin.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec()

        try:
            con = sqlite3.connect("otomatikSiparisler.db")
            cursor = con.cursor()

            cursor.execute("Select * From BanabiOtomatikSiparisler[0]")
            veri = cursor.fetchall()

            bilgiler = veri[4]
            siparisAdi = bilgiler[0]
            sehir = bilgiler[1]
            kullaniciAdi = bilgiler[2]
            parola = bilgiler[3]
            birinciParca = bilgiler [4]
            birinciParcaAdet = bilgiler [5]
            ikinciParca = bilgiler[6]
            ikinciParcaAdet = bilgiler[7]
            ucuncuParca = bilgiler[8]
            ucuncuParcaAdet = bilgiler[9]
            dorduncuParca = bilgiler[10]
            dorduncuParcaAdet = bilgiler[11]
            besinciParca = bilgiler[12]
            besinciParcaAdet = bilgiler[13]

            def operate(sehir, kullaniciAdi, parola, birinciParca, birinciParcaAdet, ikinciParca, ikinciParcaAdet, ucuncuParca, ucuncuParcaAdet, dorduncuParca, dorduncuParcaAdet, besinciParca, besinciParcaAdet):
                
                path = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(path)

                def git(sehir):
                        sehir = sehir.lower()
                        sehir = sehir.replace("ş", "s")
                        sehir = sehir.replace("ğ", "g")
                        sehir = sehir.replace("ç", "c")
                        sehir = sehir.replace("ö", "o")
                        sehir = sehir.replace("ı", "i")
                        sehir = sehir.replace("ü", "u")
                        driver.get("https://www.yemeksepeti.com/"+sehir)

                        time.sleep(1)

                        driver.maximize_window()

                        time.sleep(5)

                def giris(kullaniciAdi, parola):
                    username = driver.find_element_by_id("UserName")
                    username.send_keys(kullaniciAdi)

                    time.sleep(2)

                    password = driver.find_element_by_id("password")
                    password.send_keys(parola)

                    time.sleep(2)

                    giris = driver.find_element_by_id("ys-fastlogin-button")
                    giris.click()

                    time.sleep(3)

                def banabiGit():
                    driver.get("https://www.yemeksepeti.com/banabi")

                    time.sleep(3)

                def adresSec():
                    adres = driver.find_element_by_xpath("//*[@id='app']/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]")
                    adres.click()

                    time.sleep(3)

                def urunAra(parca):
                    ara = driver.find_element_by_class_name("search-bar-input")
                    ara.send_keys(parca)

                    time.sleep(1)

                    ara.send_keys(Keys.ENTER)

                    time.sleep(3)

                    try:
                        bekle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "return-ys-popup-close")))
                        yemeksepetiGec = driver.find_element_by_xpath("//*[@id='footer']/div[4]/div[2]/button[1]")
                        yemeksepetiGec.click()

                    except TimeoutException:
                        pass


                    

                def parcaBul(parca, parcaAdet):

                    def sepetOlustur():

                        try:
                            bekle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "product-item-details")))

                            time.sleep(3)

                        finally:
                            if (parcaAdet == 1):
                                pass
                            
                            else:
                                i = 1

                                while i < parcaAdet:
                                    ekle = driver.find_element_by_class_name("add-product-button.false")
                                    ekle.click()

                                    i += 1

                            sepeteEkle = driver.find_element_by_class_name("product-item-add-basket.false")
                            sepeteEkle.click()

                    if (parca.upper() == "HAYIR") and (parca.lower() == "hayır"):
                        pass

                    else:

                        time.sleep(3)

                        ilkSecenek = driver.find_element_by_class_name("product-list-item-title")
                        ilkSecenek.click()

                        try:
                            sepetOlustur()

                        except StaleElementReferenceException:
                            time.sleep(5)
                            
                            bekle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "product-list-item-title")))

                            time.sleep(3)

                            ilkSecenek = driver.find_element_by_class_name("product-list-item-title")
                            ilkSecenek.click()

                            time.sleep(3)

                            sepetOlustur()

                        except ElementClickInterceptedException:
                            time.sleep(5)

                            sepetOlustur()

                        except TimeoutError:
                            time.sleep(5)

                            sepetOlustur()
                
                def sepetAyarla():
                    time.sleep(7)

                    sepetOnay = driver.find_element_by_class_name("basket-confirm-button")
                    sepetOnay.click()

                    time.sleep(5)

                    kapıdaNakit = driver.find_element_by_xpath("//*[@id='content']/div/div[4]/div/div[2]/div[2]/div/label/span[3]")
                    kapıdaNakit.click()

                git(sehir)
                giris(kullaniciAdi, parola)
                banabiGit()
                adresSec()
                if birinciParca.upper() == "HAYIR":
                    pass
                else:
                    urunAra(birinciParca)
                    parcaBul(birinciParca, birinciParcaAdet)
                
                if ikinciParca.upper() == "HAYIR":
                    pass
                else:
                    urunAra(ikinciParca)
                    parcaBul(ikinciParca, ikinciParcaAdet)

                if ucuncuParca.upper() == "HAYIR":
                    pass
                else:
                    urunAra(ucuncuParca)
                    parcaBul(ucuncuParca, ucuncuParcaAdet)

                if dorduncuParca.upper() == "HAYIR":
                    pass
                else:
                    urunAra(dorduncuParca)
                    parcaBul(dorduncuParca, dorduncuParcaAdet)
                
                if besinciParca.upper() == "HAYIR":
                    pass
                else:
                    urunAra(besinciParca)
                    parcaBul(besinciParca, besinciParcaAdet)
                sepetAyarla()

            operate(sehir, kullaniciAdi, parola, birinciParca, birinciParcaAdet, ikinciParca, ikinciParcaAdet, ucuncuParca, ucuncuParcaAdet, dorduncuParca, dorduncuParcaAdet, besinciParca, besinciParcaAdet)
            popUp3(self)
        
        except IndexError:
            popUp4(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banabiSiparisEkrani5 = QtWidgets.QMainWindow()
    ui = Ui_banabiSiparisEkrani5()
    ui.setupUi(banabiSiparisEkrani5)
    banabiSiparisEkrani5.show()
    sys.exit(app.exec_())
