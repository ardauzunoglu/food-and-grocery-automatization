from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sqlite3

con = sqlite3.connect("otomatikMenuler.db")
cursor = con.cursor()

class Ui_menuEkrani3(object):
    def setupUi(self, menuEkrani3):
        menuEkrani3.setObjectName("menuEkrani3")
        menuEkrani3.resize(500, 550)

        self.centralwidget = QtWidgets.QWidget(menuEkrani3)
        self.centralwidget.setObjectName("centralwidget")

        self.siparisAdi = QtWidgets.QLabel(self.centralwidget)
        self.siparisAdi.setGeometry(QtCore.QRect(20, 20, 211, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.siparisAdi.setFont(font)
        self.siparisAdi.setObjectName("siparisAdi")

        self.kullaniciAdi = QtWidgets.QLabel(self.centralwidget)
        self.kullaniciAdi.setGeometry(QtCore.QRect(20, 70, 450, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.kullaniciAdi.setFont(font)
        self.kullaniciAdi.setObjectName("kullaniciAdi")

        self.sehir = QtWidgets.QLabel(self.centralwidget)
        self.sehir.setGeometry(QtCore.QRect(20, 120, 350, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.sehir.setFont(font)
        self.sehir.setObjectName("sehir")

        self.restoran = QtWidgets.QLabel(self.centralwidget)
        self.restoran.setGeometry(QtCore.QRect(20, 170, 350, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.restoran.setFont(font)
        self.restoran.setObjectName("restoran")

        self.birinciParca = QtWidgets.QLabel(self.centralwidget)
        self.birinciParca.setGeometry(QtCore.QRect(20, 220, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.birinciParca.setFont(font)
        self.birinciParca.setObjectName("birinciParca")

        self.ikinciParca = QtWidgets.QLabel(self.centralwidget)
        self.ikinciParca.setGeometry(QtCore.QRect(20, 270, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ikinciParca.setFont(font)
        self.ikinciParca.setObjectName("ikinciParca")

        self.ucuncuParca = QtWidgets.QLabel(self.centralwidget)
        self.ucuncuParca.setGeometry(QtCore.QRect(20, 320, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(12)

        self.ucuncuParca.setFont(font)
        self.ucuncuParca.setObjectName("ucuncuParca")

        self.siparisiSil = QtWidgets.QPushButton(self.centralwidget)
        self.siparisiSil.setGeometry(QtCore.QRect(270, 410, 181, 41))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)

        self.siparisiSil.setFont(font)
        self.siparisiSil.setStyleSheet("background-color: rgb(255, 0, 0); border: none; color: rgb(0, 0, 0);")
        self.siparisiSil.setObjectName("siparisiSil")
        self.siparisiSil.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparisiSil.clicked.connect(self.siparisiSilme)

        self.siparisVer = QtWidgets.QPushButton(self.centralwidget)
        self.siparisVer.setGeometry(QtCore.QRect(20, 410, 181, 41))

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

        self.not1 = QtWidgets.QLabel(self.centralwidget)
        self.not1.setGeometry(QtCore.QRect(20, 470, 451, 16))
        self.not1.setObjectName("not1")

        menuEkrani3.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(menuEkrani3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")

        menuEkrani3.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(menuEkrani3)
        self.statusbar.setObjectName("statusbar")

        menuEkrani3.setStatusBar(self.statusbar)

        self.retranslateUi(menuEkrani3)
        QtCore.QMetaObject.connectSlotsByName(menuEkrani3)

    def retranslateUi(self, menuEkrani3):
        cursor.execute("Select * From OtomatikSiparisler[0]")
        veri = cursor.fetchall()

        try:
            bilgiler = veri[2]
            siparisAdi = bilgiler[0]
            kullaniciAdi = bilgiler[1]
            sehir = bilgiler[3]
            restoran = bilgiler[4]
            birinciParca = bilgiler[5]
            ikinciParca = bilgiler[6]
            ucuncuParca = bilgiler[7]

            _translate = QtCore.QCoreApplication.translate
            menuEkrani3.setWindowTitle(_translate("menuEkrani3", siparisAdi))

            self.siparisAdi.setText(_translate("menuEkrani3", "Sipariş Adı:  "+siparisAdi))
            self.kullaniciAdi.setText(_translate("menuEkrani3", "Yemeksepeti Hesabı:  "+kullaniciAdi))
            self.sehir.setText(_translate("menuEkrani3", "Şehir:  "+sehir))
            self.restoran.setText(_translate("menuEkrani3", "Restoran:  "+restoran))
            self.birinciParca.setText(_translate("menuEkrani3", "Birinci Parça:  "+birinciParca))
            self.ikinciParca.setText(_translate("menuEkrani3", "İkinci Parça:  "+ikinciParca))
            self.ucuncuParca.setText(_translate("menuEkrani3", "Üçüncü Parça:  "+ucuncuParca))
            self.siparisiSil.setText(_translate("menuEkrani3", "Siparişi Sil"))
            self.siparisVer.setText(_translate("menuEkrani3", "Sipariş Ver"))
            self.not1.setText(_translate("menuEkrani3", "Not: Siparişinizde seçilmesi gereken değişkenler varsa normal seçimler seçilerek sepete eklenir."))
        
        except IndexError:
            siparisAdi = "Boş"
            kullaniciAdi = "Boş"
            sehir = "Boş"
            restoran = "Boş"
            birinciParca = "Boş"
            ikinciParca = "Boş"
            ucuncuParca = "Boş"

            _translate = QtCore.QCoreApplication.translate
            menuEkrani3.setWindowTitle(_translate("menuEkrani3", "Boş Menü"))

            self.siparisAdi.setText(_translate("menuEkrani3", "Sipariş Adı:  "+siparisAdi))
            self.kullaniciAdi.setText(_translate("menuEkrani3", "Yemeksepeti Hesabı:  "+kullaniciAdi))
            self.sehir.setText(_translate("menuEkrani3", "Şehir:  "+sehir))
            self.restoran.setText(_translate("menuEkrani3", "Restoran:  "+restoran))
            self.birinciParca.setText(_translate("menuEkrani3", "Birinci Parça:  "+birinciParca))
            self.ikinciParca.setText(_translate("menuEkrani3", "İkinci Parça:  "+ikinciParca))
            self.ucuncuParca.setText(_translate("menuEkrani3", "Üçüncü Parça:  "+ucuncuParca))
            self.siparisiSil.setText(_translate("menuEkrani3", "Siparişi Sil"))
            self.siparisVer.setText(_translate("menuEkrani3", "Sipariş Ver"))
            self.not1.setText(_translate("menuEkrani3", "Not: Siparişinizde seçilmesi gereken değişkenler varsa normal seçimler seçilerek sepete eklenir."))

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
            cursor.execute("Select * From OtomatikSiparisler[0]")
            veri = cursor.fetchall()
            bilgiler = veri[2]
            siparisAdi = bilgiler[0]
            cursor.execute("Delete From OtomatikSiparisler where Siparis_Adi = ?", (siparisAdi,))
            con.commit()
            popUp1(self)
        except IndexError:
            popUp2(self)

    def siparisVerme(self):
        def popUp3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Verildi")
            msg.setText("Seçmiş olduğunuz sipariş Yemeksepeti'nde sepetinize eklendi.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec()
        def popUp4(self):
            msg = QMessageBox()
            msg.setWindowTitle("Sipariş Verilemedi")
            msg.setText("Seçmiş olduğunuz sipariş boş, lütfen yeni bir sipariş oluşturun ya da var olan bir sipariş verin.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec()
        try:
            con = sqlite3.connect("otomatikMenuler.db")
            cursor = con.cursor()

            cursor.execute("Select * From OtomatikSiparisler[0]")
            veri = cursor.fetchall()

            bilgiler = veri[2]
            siparisAdi = bilgiler[0]
            kullaniciAdi = bilgiler[1]
            parola = bilgiler[2]
            sehir = bilgiler[3]
            restoran = bilgiler[4]
            birinciParca = bilgiler[5]
            ikinciParca = bilgiler[6]
            ucuncuParca = bilgiler[7]
            def operate(sehir, kullaniciAdi, parola, restoran, birinciParca, ikinciParca, ucuncuParca):

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

                def evButonu():

                    bekle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "address-labels")))

                    evButonu = driver.find_element_by_class_name("address-labels")
                    evButonu.click()

                    time.sleep(5)

                def restoranAra(restoran):
                    ara = driver.find_element_by_class_name("search-box")
                    ara.send_keys(restoran)

                    time.sleep(1)

                    araButon = driver.find_element_by_class_name("search-button")
                    araButon.click()

                    time.sleep(3)

                def restoranaGir():
                    restoranaGiris = driver.find_element_by_class_name("restaurantName")
                    restoranaGiris.click()

                    time.sleep(5)

                def parcaBul(parca):

                    def sepetOlustur():

                            bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, parca)))

                            try:                        
                                bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cboxLoadedContent")))

                                time.sleep(3)
                                
                                secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                                time.sleep(3)

                                for secenek in secenekler:

                                    sec = Select(secenek)
                                    sec.select_by_index(1)

                                time.sleep(3)

                                secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                                time.sleep(3)

                                for secenek in secenekler:

                                    sec = Select(secenek)
                                    sec.select_by_index(1)

                                time.sleep(3)

                            except ElementNotInteractableException:

                                time.sleep(5)

                                araEkran = driver.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[1]/div/div/div[2]")
                                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", araEkran)

                                time.sleep(3)

                                secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                                time.sleep(3)

                                for secenek in secenekler:

                                    sec = Select(secenek)
                                    sec.select_by_index(1)

                                time.sleep(3)

                                secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                                time.sleep(3)

                                for secenek in secenekler:

                                    sec = Select(secenek)
                                    sec.select_by_index(1)

                                time.sleep(3)

                            finally:

                                time.sleep(3)

                                sepeteEkle = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/button")
                                sepeteEkle.click()

                                time.sleep(3)

                                driver.execute_script("window.scroll(0, 0);")

                                time.sleep(3)

                    if (parca.upper() == "HAYIR"):
                        pass

                    else:
                        parcaSecimi = driver.find_element_by_link_text(parca)
                        parcaSecimi.click()
                        try:
                            sepetOlustur()

                        except StaleElementReferenceException:

                            time.sleep(5)
                            
                            bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, parca)))

                            time.sleep(3)

                            parcaSecimi = driver.find_element_by_link_text(parca)
                            parcaSecimi.click()

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

                    sepetOnay = driver.find_element_by_class_name("confirm-basket")
                    sepetOnay.click()

                    time.sleep(12)

                    kapidaNakit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[9]/div/div/div/div/div[2]/div/div[2]/label/input")
                    kapidaNakit.click()


                git(sehir)
                giris(kullaniciAdi, parola)
                evButonu()
                restoranAra(restoran)
                restoranaGir()
                parcaBul(birinciParca)
                parcaBul(ikinciParca)
                parcaBul(ucuncuParca)
                sepetAyarla()

            operate(sehir, kullaniciAdi, parola, restoran, birinciParca, ikinciParca, ucuncuParca)
            popUp3(self)
        except IndexError:
            popUp4(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuEkrani3 = QtWidgets.QMainWindow()
    ui = Ui_menuEkrani3()
    ui.setupUi(menuEkrani3)
    menuEkrani3.show()
    sys.exit(app.exec_())