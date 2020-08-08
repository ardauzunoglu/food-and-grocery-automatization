from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from banabiSiparisEkrani1 import Ui_banabiSiparisEkrani1
from banabiSiparisEkrani2 import Ui_banabiSiparisEkrani2
from banabiSiparisEkrani3 import Ui_banabiSiparisEkrani3
from banabiSiparisEkrani4 import Ui_banabiSiparisEkrani4
from banabiSiparisEkrani5 import Ui_banabiSiparisEkrani5
from banabiSiparisEkrani6 import Ui_banabiSiparisEkrani6
from banabiSiparisEkrani7 import Ui_banabiSiparisEkrani7
from banabiSiparisEkrani8 import Ui_banabiSiparisEkrani8
from banabiSiparisEkrani9 import Ui_banabiSiparisEkrani9
from banabiSiparisEkrani10 import Ui_banabiSiparisEkrani10
import sqlite3

con = sqlite3.connect("otomatikSiparisler.db")
cursor = con.cursor()

class Ui_banabiSiparisVer(object):

    def banabiSiparisEkrani1Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani1()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani2Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani2()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani3Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani3()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani4Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani4()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani5Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani5()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani6Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani6()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani7Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani7()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani8Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani8()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani9Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani9()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisEkrani10Ac(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisEkrani10()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def setupUi(self, banabiSiparisVer):
        banabiSiparisVer.setObjectName("banabiSiparisVer")
        banabiSiparisVer.resize(600, 650)

        self.centralwidget = QtWidgets.QWidget(banabiSiparisVer)
        self.centralwidget.setObjectName("centralwidget")

        self.siparis1 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis1.setGeometry(QtCore.QRect(70, 40, 151, 51))
        self.siparis1.setObjectName("siparis1")
        self.siparis1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis1.clicked.connect(self.banabiSiparisEkrani1Ac)

        self.siparis2 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis2.setGeometry(QtCore.QRect(70, 160, 151, 51))
        self.siparis2.setObjectName("siparis2")
        self.siparis2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis2.clicked.connect(self.banabiSiparisEkrani2Ac)

        self.siparis3 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis3.setGeometry(QtCore.QRect(70, 280, 151, 51))
        self.siparis3.setObjectName("siparis3")
        self.siparis3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis3.clicked.connect(self.banabiSiparisEkrani3Ac)

        self.siparis4 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis4.setGeometry(QtCore.QRect(70, 400, 151, 51))
        self.siparis4.setObjectName("siparis4")
        self.siparis4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis4.clicked.connect(self.banabiSiparisEkrani4Ac)

        self.siparis5 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis5.setGeometry(QtCore.QRect(70, 520, 151, 51))
        self.siparis5.setObjectName("siparis5")
        self.siparis5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis5.clicked.connect(self.banabiSiparisEkrani5Ac)

        self.siparis6 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis6.setGeometry(QtCore.QRect(380, 40, 151, 51))
        self.siparis6.setObjectName("siparis6")
        self.siparis6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis6.clicked.connect(self.banabiSiparisEkrani6Ac)

        self.siparis7 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis7.setGeometry(QtCore.QRect(380, 160, 151, 51))
        self.siparis7.setObjectName("siparis7")
        self.siparis7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis7.clicked.connect(self.banabiSiparisEkrani7Ac)

        self.siparis8 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis8.setGeometry(QtCore.QRect(380, 280, 151, 51))
        self.siparis8.setObjectName("siparis8")
        self.siparis8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis8.clicked.connect(self.banabiSiparisEkrani8Ac)

        self.siparis9 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis9.setGeometry(QtCore.QRect(380, 400, 151, 51))
        self.siparis9.setObjectName("siparis9")
        self.siparis9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis9.clicked.connect(self.banabiSiparisEkrani9Ac)

        self.siparis10 = QtWidgets.QPushButton(self.centralwidget)
        self.siparis10.setGeometry(QtCore.QRect(380, 520, 151, 51))
        self.siparis10.setObjectName("siparis10")
        self.siparis10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparis10.clicked.connect(self.banabiSiparisEkrani10Ac)

        banabiSiparisVer.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(banabiSiparisVer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        banabiSiparisVer.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(banabiSiparisVer)
        self.statusbar.setObjectName("statusbar")

        banabiSiparisVer.setStatusBar(self.statusbar)

        self.retranslateUi(banabiSiparisVer)
        QtCore.QMetaObject.connectSlotsByName(banabiSiparisVer)

    def retranslateUi(self, banabiSiparisVer):
        siparisAdlari = []
        cursor.execute("Select Siparis_Adi From BanabiOtomatikSiparisler")
        veri = cursor.fetchall()

        def convertTuple(tup): 
            str =  ''.join(tup) 
            return str

        for i in veri:  
            i = convertTuple(i)
            siparisAdlari.append(i)

        _translate = QtCore.QCoreApplication.translate
        banabiSiparisVer.setWindowTitle(_translate("siparisVer", "Sipariş Ver"))

        if (len(siparisAdlari) == 0):
            self.siparis1.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis2.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis3.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis4.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis5.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 1):
            Siparis1 = str(siparisAdlari[0])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis3.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis4.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis5.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 2):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis4.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis5.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 3):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis5.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 4):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 5):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            Siparis5 = str(siparisAdlari[4])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 6):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            Siparis5 = str(siparisAdlari[4])
            Siparis6 = str(siparisAdlari[5])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", Siparis6))
            self.siparis7.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 7):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            Siparis5 = str(siparisAdlari[4])
            Siparis6 = str(siparisAdlari[5])
            Siparis7 = str(siparisAdlari[6])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", Siparis6))
            self.siparis7.setText(_translate("banabiSiparisVer", Siparis7))
            self.siparis8.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        elif (len(siparisAdlari) == 8):
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            Siparis5 = str(siparisAdlari[4])
            Siparis6 = str(siparisAdlari[5])
            Siparis7 = str(siparisAdlari[6])
            Siparis8 = str(siparisAdlari[7])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", Siparis6))
            self.siparis7.setText(_translate("banabiSiparisVer", Siparis7))
            self.siparis8.setText(_translate("banabiSiparisVer", Siparis8))
            self.siparis9.setText(_translate("banabiSiparisVer", "Boş Sipariş"))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

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

            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", Siparis6))
            self.siparis7.setText(_translate("banabiSiparisVer", Siparis7))
            self.siparis8.setText(_translate("banabiSiparisVer", Siparis8))
            self.siparis9.setText(_translate("banabiSiparisVer", Siparis9))
            self.siparis10.setText(_translate("banabiSiparisVer", "Boş Sipariş"))

        else:
            Siparis1 = str(siparisAdlari[0])
            Siparis2 = str(siparisAdlari[1])
            Siparis3 = str(siparisAdlari[2])
            Siparis4 = str(siparisAdlari[3])
            Siparis5 = str(siparisAdlari[4])
            Siparis6 = str(siparisAdlari[5])
            Siparis7 = str(siparisAdlari[6])
            Siparis8 = str(siparisAdlari[7])
            Siparis9 = str(siparisAdlari[8])
            Siparis10 = str(siparisAdlari[9])
            self.siparis1.setText(_translate("banabiSiparisVer", Siparis1))
            self.siparis2.setText(_translate("banabiSiparisVer", Siparis2))
            self.siparis3.setText(_translate("banabiSiparisVer", Siparis3))
            self.siparis4.setText(_translate("banabiSiparisVer", Siparis4))
            self.siparis5.setText(_translate("banabiSiparisVer", Siparis5))
            self.siparis6.setText(_translate("banabiSiparisVer", Siparis6))
            self.siparis7.setText(_translate("banabiSiparisVer", Siparis7))
            self.siparis8.setText(_translate("banabiSiparisVer", Siparis8))
            self.siparis9.setText(_translate("banabiSiparisVer", Siparis9))
            self.siparis10.setText(_translate("banabiSiparisVer", Siparis10))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banabiSiparisVer = QtWidgets.QMainWindow()
    ui = Ui_banabiSiparisVer()
    ui.setupUi(banabiSiparisVer)
    banabiSiparisVer.show()
    sys.exit(app.exec_())
