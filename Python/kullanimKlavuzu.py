from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kullanimKlavuzu(object):
    def setupUi(self, kullanimKlavuzu):
        kullanimKlavuzu.setObjectName("kullanimKlavuzu")
        kullanimKlavuzu.resize(600, 650)

        self.centralwidget = QtWidgets.QWidget(kullanimKlavuzu)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 0, 531, 41))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(18)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 470, 21))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 431, 16))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 480, 431, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 400, 431, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 360, 431, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 290, 431, 20))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)

        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 50, 431, 21))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 431, 21))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 180, 431, 21))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 450, 431, 20))

        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)

        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 510, 431, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 540, 551, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 570, 551, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 230, 551, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        kullanimKlavuzu.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(kullanimKlavuzu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        kullanimKlavuzu.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(kullanimKlavuzu)
        self.statusbar.setObjectName("statusbar")

        kullanimKlavuzu.setStatusBar(self.statusbar)

        self.retranslateUi(kullanimKlavuzu)
        QtCore.QMetaObject.connectSlotsByName(kullanimKlavuzu)

    def retranslateUi(self, kullanimKlavuzu):
        _translate = QtCore.QCoreApplication.translate
        kullanimKlavuzu.setWindowTitle(_translate("kullanimKlavuzu", "Kullanım Klavuzu"))

        self.label.setText(_translate("kullanimKlavuzu", "Yemeksepeti Otomatizasyonu Kullanım Klavuzu"))

        self.label_2.setText(_translate("kullanimKlavuzu", "- Sipariş vermek için önceden oluşturduğunuz otomatik siparişleri kullanmalısınız."))

        self.label_3.setText(_translate("kullanimKlavuzu", "- Yemeksepeti Optimizasyonu penceresine gelin."))

        self.label_4.setText(_translate("kullanimKlavuzu", "- En fazla beş adet otomatik sipariş oluşturabilirsiniz."))

        self.label_5.setText(_translate("kullanimKlavuzu", "- İstenilen bilgileri doldurup 'Oluştur' butonuna tıklayın."))

        self.label_7.setText(_translate("kullanimKlavuzu", "- Otomatik Sipariş Oluştur butonuna tıklayın."))

        self.label_8.setText(_translate("kullanimKlavuzu", "Otomatik Sipariş oluşturmak için:"))

        self.label_9.setText(_translate("kullanimKlavuzu", "Sipariş vermek için:"))

        self.label_6.setText(_translate("kullanimKlavuzu", "- Yemeksepeti Optimizasyonu penceresine gelin."))

        self.label_10.setText(_translate("kullanimKlavuzu", "- Önceden oluşturduğunuz siparişlerden istediğinizi seçin."))

        self.label_15.setText(_translate("kullanimKlavuzu", "- 'Sipariş Ver' butonunu kullanarak siparişinizi tamamlayın."))

        self.label_11.setText(_translate("kullanimKlavuzu", "Notlar: "))

        self.label_12.setText(_translate("kullanimKlavuzu", "- Tek bir siparişte en fazla üç parça sipariş edebilirsiniz."))

        self.label_13.setText(_translate("kullanimKlavuzu", "- Eğer sipariş ettiğiniz parçada seçilmesi gereken değer varsa normal değer seçilir."))

        self.label_14.setText(_translate("kullanimKlavuzu", "- Seçtiğiniz parçalar sepetinize eklenir, istediğiniz değişikliği yapabilir ve sepetinizi onaylayabilirsiniz."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kullanimKlavuzu = QtWidgets.QMainWindow()
    ui = Ui_kullanimKlavuzu()
    ui.setupUi(kullanimKlavuzu)
    kullanimKlavuzu.show()
    sys.exit(app.exec_())
