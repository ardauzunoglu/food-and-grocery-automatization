from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from yemeksepetiSiparisOtomatizasyonu import Ui_yemeksepetiSiparisOtomatizasyonu
from banabiAnaEkran import Ui_banabiAnaEkran

class Ui_MainWindow(object):

    def yemeksepetiSiparisOtomatizasyonuAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_yemeksepetiSiparisOtomatizasyonu()
        self.ui.setupUi(self.window)
        self.window.show()

    def banabiAnaEkranAc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_banabiAnaEkran()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("anaEkran")
        MainWindow.resize(500, 275)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 411, 41))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 130, 175, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 130, 175, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.yemeksepetiSiparisOtomatizasyonuAc)
        self.pushButton_2.clicked.connect(self.banabiAnaEkranAc)
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Ekran"))
        self.label.setText(_translate("MainWindow", "Hangi uygulamayı kullanacaksınız?"))
        self.pushButton.setText(_translate("MainWindow", "Yemeksepeti"))
        self.pushButton_2.setText(_translate("MainWindow", "Banabi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
