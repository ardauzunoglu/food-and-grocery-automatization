from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_banabiKullanimKlavuzu(object):
    def setupUi(self, banabiKullanimKlavuzu):
        banabiKullanimKlavuzu.setObjectName("banabiKullanimKlavuzu")
        banabiKullanimKlavuzu.resize(600, 650)

        self.centralwidget = QtWidgets.QWidget(banabiKullanimKlavuzu)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 0, 531, 41))

        font = QtGui.QFont()
        font.setFamily("Muli")
        font.setPointSize(18)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 471, 21))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 431, 16))

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
        self.label_5.setGeometry(QtCore.QRect(50, 360, 431, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 310, 431, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 240, 431, 20))

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

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 540, 551, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(50, 570, 551, 21))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        banabiKullanimKlavuzu.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(banabiKullanimKlavuzu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")

        banabiKullanimKlavuzu.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(banabiKullanimKlavuzu)
        self.statusbar.setObjectName("statusbar")

        banabiKullanimKlavuzu.setStatusBar(self.statusbar)

        self.retranslateUi(banabiKullanimKlavuzu)
        QtCore.QMetaObject.connectSlotsByName(banabiKullanimKlavuzu)

    def retranslateUi(self, banabiKullanimKlavuzu):
        _translate = QtCore.QCoreApplication.translate
        banabiKullanimKlavuzu.setWindowTitle(_translate("banabiKullanimKlavuzu", "Kullanım Klavuzu"))
        self.label.setText(_translate("banabiKullanimKlavuzu", "Banabi Otomatizasyonu Kullanım Klavuzu"))
        self.label_2.setText(_translate("banabiKullanimKlavuzu", "- Sipariş vermek için önceden oluşturduğunuz otomatik siparişleri kullanmalısınız."))
        self.label_3.setText(_translate("banabiKullanimKlavuzu", "- Banabi Optimizasyonu penceresine gelin."))
        self.label_4.setText(_translate("MainbanabiKullanimKlavuzuWindow", "- En fazla on adet otomatik sipariş oluşturabilirsiniz."))
        self.label_5.setText(_translate("banabiKullanimKlavuzu", "- İstenilen bilgileri doldurun."))
        self.label_7.setText(_translate("banabiKullanimKlavuzu", "- Otomatik Sipariş Oluştur butonuna tıklayın."))
        self.label_8.setText(_translate("banabiKullanimKlavuzu", "Otomatik Sipariş oluşturmak için:"))
        self.label_9.setText(_translate("banabiKullanimKlavuzu", "Sipariş vermek için:"))
        self.label_6.setText(_translate("banabiKullanimKlavuzu", "- Banabi Optimizasyonu penceresine gelin."))
        self.label_10.setText(_translate("banabiKullanimKlavuzu", "- Önceden oluşturduğunuz siparişlerden istediğinize tıklayarak sipariş edin."))
        self.label_11.setText(_translate("banabiKullanimKlavuzu", "Notlar: "))
        self.label_12.setText(_translate("banabiKullanimKlavuzu", "- Tek bir siparişte en fazla beş parça sipariş edebilirsiniz."))
        self.label_14.setText(_translate("banabiKullanimKlavuzu", "- Seçtiğiniz parçalar sepetinize eklenir, istediğiniz değişikliği yapabilir ve sepetinizi onaylayabilirsiniz."))
        self.label_16.setText(_translate("banabiKullanimKlavuzu", "- Hesabınıza Banabi'nin hizmet kapsamında bulunan bir adres bağlı olmalıdır."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banabiKullanimKlavuzu = QtWidgets.QMainWindow()
    ui = Ui_banabiKullanimKlavuzu()
    ui.setupUi(banabiKullanimKlavuzu)
    banabiKullanimKlavuzu.show()
    sys.exit(app.exec_())
