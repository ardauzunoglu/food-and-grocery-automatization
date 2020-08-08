from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from kullanimKlavuzu import Ui_kullanimKlavuzu
from otomatikSiparisOlustur import Ui_otomatikSiparisOlustur
from siparisVer import Ui_siparisVer

class Ui_yemeksepetiSiparisOtomatizasyonu(object):
    def kullanimKlavuzuAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_kullanimKlavuzu()
        self.ui.setupUi(self.window)
        self.window.show()

    def otomatikSiparisOlusturAc(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_otomatikSiparisOlustur()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def siparisVerAc(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_siparisVer()
        self.ui.setupUi(self.pencere)
        self.pencere.show()


    def setupUi(self, yemeksepetiSiparisOtomatizasyonu):
        yemeksepetiSiparisOtomatizasyonu.setObjectName("yemeksepetiSiparisOtomatizasyonu")
        yemeksepetiSiparisOtomatizasyonu.resize(600, 375)

        self.yemeksepetiOtomatizasyonu = QtWidgets.QWidget(yemeksepetiSiparisOtomatizasyonu)
        self.yemeksepetiOtomatizasyonu.setObjectName("yemeksepetiOtomatizasyonu")
        self.label = QtWidgets.QLabel(self.yemeksepetiOtomatizasyonu)
        self.label.setGeometry(QtCore.QRect(80, 30, 455, 41))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(24)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.otomatikSiparisOlustur = QtWidgets.QPushButton(self.yemeksepetiOtomatizasyonu)
        self.otomatikSiparisOlustur.setGeometry(QtCore.QRect(80, 110, 181, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.otomatikSiparisOlustur.setFont(font)
        self.otomatikSiparisOlustur.setObjectName("otomatikSiparisOlustur")
        self.otomatikSiparisOlustur.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.otomatikSiparisOlustur.clicked.connect(self.otomatikSiparisOlusturAc)

        self.siparisVer = QtWidgets.QPushButton(self.yemeksepetiOtomatizasyonu)
        self.siparisVer.setGeometry(QtCore.QRect(330, 110, 181, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.siparisVer.setFont(font)
        self.siparisVer.setObjectName("siparisVer")
        self.siparisVer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparisVer.clicked.connect(self.siparisVerAc)

        self.kullanimKlavuzu = QtWidgets.QPushButton(self.yemeksepetiOtomatizasyonu)
        self.kullanimKlavuzu.setGeometry(QtCore.QRect(80, 160, 431, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.kullanimKlavuzu.setFont(font)
        self.kullanimKlavuzu.setObjectName("kullanimKlavuzu")
        self.kullanimKlavuzu.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.kullanimKlavuzu.clicked.connect(self.kullanimKlavuzuAc)

        self.label_2 = QtWidgets.QLabel(self.yemeksepetiOtomatizasyonu)
        self.label_2.setGeometry(QtCore.QRect(210, 310, 170, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        yemeksepetiSiparisOtomatizasyonu.setCentralWidget(self.yemeksepetiOtomatizasyonu)

        self.menubar = QtWidgets.QMenuBar(yemeksepetiSiparisOtomatizasyonu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        yemeksepetiSiparisOtomatizasyonu.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(yemeksepetiSiparisOtomatizasyonu)
        self.statusbar.setObjectName("statusbar")

        yemeksepetiSiparisOtomatizasyonu.setStatusBar(self.statusbar)

        self.retranslateUi(yemeksepetiSiparisOtomatizasyonu)
        QtCore.QMetaObject.connectSlotsByName(yemeksepetiSiparisOtomatizasyonu)

    def retranslateUi(self, yemeksepetiSiparisOtomatizasyonu):
        _translate = QtCore.QCoreApplication.translate
        yemeksepetiSiparisOtomatizasyonu.setWindowTitle(_translate("yemeksepetiSiparisOtomatizasyonu", "Yemeksepeti Otomatizasyonu"))
        self.label.setText(_translate("yemeksepetiSiparisOtomatizasyonu", "Yemeksepeti Otomatizasyonu"))
        self.otomatikSiparisOlustur.setText(_translate("yemeksepetiSiparisOtomatizasyonu", "Otomatik Sipariş Oluştur"))
        self.siparisVer.setText(_translate("yemeksepetiSiparisOtomatizasyonu", "Sipariş Ver"))
        self.kullanimKlavuzu.setText(_translate("yemeksepetiSiparisOtomatizasyonu", "Kullanım Klavuzu"))
        self.label_2.setText(_translate("yemeksepetiSiparisOtomatizasyonu", "Geliştirici: Arda Uzunoğlu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    yemeksepetiSiparisOtomatizasyonu = QtWidgets.QMainWindow()
    ui = Ui_yemeksepetiSiparisOtomatizasyonu()
    ui.setupUi(yemeksepetiSiparisOtomatizasyonu)
    yemeksepetiSiparisOtomatizasyonu.show()
    sys.exit(app.exec_())
