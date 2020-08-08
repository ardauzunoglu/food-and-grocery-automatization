from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from banabiKullanimKlavuzu import Ui_banabiKullanimKlavuzu
from banabiOtomatikSiparisOlustur import Ui_banabiOtomatikSiparisOlustur
from banabiSiparisVer import Ui_banabiSiparisVer


class Ui_banabiAnaEkran(object):

    def banabiKullanimKlavuzuAc(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiKullanimKlavuzu()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiOtomatikSiparisOlusturAc(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiOtomatikSiparisOlustur()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def banabiSiparisVer(self):
        self.pencere = QtWidgets.QMainWindow()
        self.ui = Ui_banabiSiparisVer()
        self.ui.setupUi(self.pencere)
        self.pencere.show()

    def setupUi(self, banabiAnaEkran):
        banabiAnaEkran.setObjectName("banabiAnaEkran")
        banabiAnaEkran.resize(600, 375)

        self.banabiOtomatizasyonu = QtWidgets.QWidget(banabiAnaEkran)
        self.banabiOtomatizasyonu.setObjectName("banabiOtomatizasyonu")

        self.label = QtWidgets.QLabel(self.banabiOtomatizasyonu)
        self.label.setGeometry(QtCore.QRect(110, 30, 375, 41))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(24)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.otomatikSiparisOlustur = QtWidgets.QPushButton(self.banabiOtomatizasyonu)
        self.otomatikSiparisOlustur.setGeometry(QtCore.QRect(110, 100, 161, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.otomatikSiparisOlustur.setFont(font)
        self.otomatikSiparisOlustur.setObjectName("otomatikSiparisOlustur")

        self.otomatikSiparisOlustur.clicked.connect(self.banabiOtomatikSiparisOlusturAc)
        self.otomatikSiparisOlustur.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.siparisVer = QtWidgets.QPushButton(self.banabiOtomatizasyonu)
        self.siparisVer.setGeometry(QtCore.QRect(310, 100, 161, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.siparisVer.setFont(font)
        self.siparisVer.setObjectName("siparisVer")

        self.siparisVer.clicked.connect(self.banabiSiparisVer)
        self.siparisVer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.kullanimKlavuzu = QtWidgets.QPushButton(self.banabiOtomatizasyonu)
        self.kullanimKlavuzu.setGeometry(QtCore.QRect(110, 160, 361, 41))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.kullanimKlavuzu.setFont(font)
        self.kullanimKlavuzu.setObjectName("kullanimKlavuzu")

        self.kullanimKlavuzu.clicked.connect(self.banabiKullanimKlavuzuAc)
        self.kullanimKlavuzu.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.label_2 = QtWidgets.QLabel(self.banabiOtomatizasyonu)
        self.label_2.setGeometry(QtCore.QRect(210, 310, 175, 16))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        banabiAnaEkran.setCentralWidget(self.banabiOtomatizasyonu)

        self.menubar = QtWidgets.QMenuBar(banabiAnaEkran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        banabiAnaEkran.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(banabiAnaEkran)
        self.statusbar.setObjectName("statusbar")

        banabiAnaEkran.setStatusBar(self.statusbar)

        self.retranslateUi(banabiAnaEkran)
        QtCore.QMetaObject.connectSlotsByName(banabiAnaEkran)

    def retranslateUi(self, banabiAnaEkran):
        _translate = QtCore.QCoreApplication.translate
        banabiAnaEkran.setWindowTitle(_translate("banabiAnaEkran", "Banabi Otomatizasyonu"))
        self.label.setText(_translate("banabiAnaEkran", "Banabi Otomatizasyonu"))
        self.otomatikSiparisOlustur.setText(_translate("banabiAnaEkran", "Otomatik Sipariş Oluştur"))
        self.siparisVer.setText(_translate("banabiAnaEkran", "Sipariş Ver"))
        self.kullanimKlavuzu.setText(_translate("banabiAnaEkran", "Kullanım Klavuzu"))
        self.label_2.setText(_translate("banabiAnaEkran", "Geliştirici: Arda Uzunoğlu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banabiAnaEkran = QtWidgets.QMainWindow()
    ui = Ui_banabiAnaEkran()
    ui.setupUi(banabiAnaEkran)
    banabiAnaEkran.show()
    sys.exit(app.exec_())
