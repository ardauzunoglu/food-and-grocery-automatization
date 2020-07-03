from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
import time
import sqlite3

con = sqlite3.connect("otomatikMenuler.db")
cursor = con.cursor()

cursor.execute("Select * From OtomatikSiparisler[0]")
veri = cursor.fetchall()

bilgiler = veri[0]
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

            time.sleep(3)

    def giris(kullaniciAdi, parola):
        username = driver.find_element_by_id("UserName")
        username.send_keys(kullaniciAdi)

        time.sleep(1)

        password = driver.find_element_by_id("password")
        password.send_keys(parola)

        time.sleep(1)

        giris = driver.find_element_by_id("ys-fastlogin-button")
        giris.click()

        time.sleep(3)

    def evButonu():
        evButonu = driver.find_element_by_class_name("address-labels")
        evButonu.click()

        time.sleep(3)

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

        time.sleep(3)

    def parcaBul1(birinciParca):
        parca1Secimi = driver.find_element_by_link_text(birinciParca)
        parca1Secimi.click()

        time.sleep(5)

        sepeteEkle = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]")
        sepeteEkle.click()

        time.sleep(3)

    def parcaBul2(ikinciParca):

        if (ikinciParca.upper() == "HAYIR"):
            pass
        else:
            parca2Secimi = driver.find_element_by_link_text(ikinciParca)
            parca2Secimi.click()

            time.sleep(5)

            sepeteEkle = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/button")
            sepeteEkle.click()

            time.sleep(3)

    def parcaBul3(ucuncuParca):
        if (ucuncuParca.upper() == "HAYIR"):
            pass
        else:
            parca3Secimi = driver.find_element_by_link_text(ucuncuParca)
            parca3Secimi.click()

            time.sleep(5)

            sepeteEkle = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/button")
            sepeteEkle.click()

            time.sleep(3)

    def sepetAyarla():
        time.sleep(5)

        sepetOnay = driver.find_element_by_class_name("confirm-basket")
        sepetOnay.click()

        time.sleep(5)

        kapidaNakit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[9]/div/div/div/div/div[2]/div/div[2]/label/input")
        kapidaNakit.click()

    git(sehir)
    giris(kullaniciAdi, parola)
    evButonu()
    restoranAra(restoran)
    restoranaGir()
    parcaBul1(birinciParca)
    parcaBul2(ikinciParca)
    parcaBul3(ucuncuParca)
    sepetAyarla()

operate(sehir, kullaniciAdi, parola, restoran, birinciParca, ikinciParca, ucuncuParca)