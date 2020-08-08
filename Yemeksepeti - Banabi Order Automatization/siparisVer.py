from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from menuEkrani1 import Ui_menuEkrani1
from menuEkrani2 import Ui_menuEkrani2
from menuEkrani3 import Ui_menuEkrani3
from menuEkrani4 import Ui_menuEkrani4
from menuEkrani5 import Ui_menuEkrani5
import sqlite3

con = sqlite3.connect("otomatikMenuler.db")
cursor = con.cursor()

class Ui_siparisVer(object):

    def menuEkrani1Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_menuEkrani1()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def menuEkrani2Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_menuEkrani2()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def menuEkrani3Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_menuEkrani3()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def menuEkrani4Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_menuEkrani4()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def menuEkrani5Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_menuEkrani5()
        self.ui.setupUi(self.pencere)
        self.pencere.show()


    def setupUi(self, siparisVer):
        siparisVer.setObjectName("siparisVer")
        siparisVer.resize(600, 650)

        self.centralwidget = QtWidgets.QWidget(siparisVer)
        self.centralwidget.setObjectName("centralwidget")

        self.menu1 = QtWidgets.QPushButton(self.centralwidget)
        self.menu1.setGeometry(QtCore.QRect(200, 75, 191, 51))
        self.menu1.setObjectName("menu1")
        self.menu1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.menu1.clicked.connect(self.menuEkrani1Ac)

        self.menu2 = QtWidgets.QPushButton(self.centralwidget)
        self.menu2.setGeometry(QtCore.QRect(200, 185, 191, 51))
        self.menu2.setObjectName("menu2")
        self.menu2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.menu2.clicked.connect(self.menuEkrani2Ac)

        self.menu3 = QtWidgets.QPushButton(self.centralwidget)
        self.menu3.setGeometry(QtCore.QRect(200, 295, 191, 51))
        self.menu3.setObjectName("menu3")
        self.menu3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.menu3.clicked.connect(self.menuEkrani3Ac)

        self.menu4 = QtWidgets.QPushButton(self.centralwidget)
        self.menu4.setGeometry(QtCore.QRect(200, 405, 191, 51))
        self.menu4.setObjectName("menu4")
        self.menu4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.menu4.clicked.connect(self.menuEkrani4Ac)

        self.menu5 = QtWidgets.QPushButton(self.centralwidget)
        self.menu5.setGeometry(QtCore.QRect(200, 515, 191, 51))
        self.menu5.setObjectName("menu5")
        self.menu5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.menu5.clicked.connect(self.menuEkrani5Ac)

        siparisVer.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(siparisVer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        siparisVer.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(siparisVer)
        self.statusbar.setObjectName("statusbar")

        siparisVer.setStatusBar(self.statusbar)

        self.retranslateUi(siparisVer)
        QtCore.QMetaObject.connectSlotsByName(siparisVer)

    def retranslateUi(self, siparisVer):
        siparisAdlari = []
        cursor.execute("Select Siparis_Adi From OtomatikSiparisler")
        veri = cursor.fetchall()

        def convertTuple(tup): 
            str =  ''.join(tup) 
            return str

        for i in veri:  
            i = convertTuple(i)
            siparisAdlari.append(i)

        _translate = QtCore.QCoreApplication.translate
        siparisVer.setWindowTitle(_translate("siparisVer", "Sipariş Ver"))

        if (len(siparisAdlari) == 0):
            self.menu1.setText(_translate("siparisVer", "Boş Menü"))
            self.menu2.setText(_translate("siparisVer", "Boş Menü"))
            self.menu3.setText(_translate("siparisVer", "Boş Menü"))
            self.menu4.setText(_translate("siparisVer", "Boş Menü"))
            self.menu5.setText(_translate("siparisVer", "Boş Menü"))
        elif (len(siparisAdlari) == 1):
            Menu1 = str(siparisAdlari[0])
            self.menu1.setText(_translate("siparisVer", Menu1))
            self.menu2.setText(_translate("siparisVer", "Boş Menü"))
            self.menu3.setText(_translate("siparisVer", "Boş Menü"))
            self.menu4.setText(_translate("siparisVer", "Boş Menü"))
            self.menu5.setText(_translate("siparisVer", "Boş Menü"))
        elif (len(siparisAdlari) == 2):
            Menu1 = str(siparisAdlari[0])
            Menu2 = str(siparisAdlari[1])
            self.menu1.setText(_translate("siparisVer", Menu1))
            self.menu2.setText(_translate("siparisVer", Menu2))
            self.menu3.setText(_translate("siparisVer", "Boş Menü"))
            self.menu4.setText(_translate("siparisVer", "Boş Menü"))
            self.menu5.setText(_translate("siparisVer", "Boş Menü"))
        elif (len(siparisAdlari) == 3):
            Menu1 = str(siparisAdlari[0])
            Menu2 = str(siparisAdlari[1])
            Menu3 = str(siparisAdlari[2])
            self.menu1.setText(_translate("siparisVer", Menu1))
            self.menu2.setText(_translate("siparisVer", Menu2))
            self.menu3.setText(_translate("siparisVer", Menu3))
            self.menu4.setText(_translate("siparisVer", "Boş Menü"))
            self.menu5.setText(_translate("siparisVer", "Boş Menü"))
        elif (len(siparisAdlari) == 4):
            Menu1 = str(siparisAdlari[0])
            Menu2 = str(siparisAdlari[1])
            Menu3 = str(siparisAdlari[2])
            Menu4 = str(siparisAdlari[3])
            self.menu1.setText(_translate("siparisVer", Menu1))
            self.menu2.setText(_translate("siparisVer", Menu2))
            self.menu3.setText(_translate("siparisVer", Menu3))
            self.menu4.setText(_translate("siparisVer", Menu4))
            self.menu5.setText(_translate("siparisVer", "Boş Menü"))
        else:
            Menu1 = str(siparisAdlari[0])
            Menu2 = str(siparisAdlari[1])
            Menu3 = str(siparisAdlari[2])
            Menu4 = str(siparisAdlari[3])
            Menu5 = str(siparisAdlari[4])
            self.menu1.setText(_translate("siparisVer", Menu1))
            self.menu2.setText(_translate("siparisVer", Menu2))
            self.menu3.setText(_translate("siparisVer", Menu3))
            self.menu4.setText(_translate("siparisVer", Menu4))
            self.menu5.setText(_translate("siparisVer", Menu5))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    siparisVer = QtWidgets.QMainWindow()
    ui = Ui_siparisVer()
    ui.setupUi(siparisVer)
    siparisVer.show()
    sys.exit(app.exec_())
