# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F3(object):
    def setupUi(self, F3):
        F3.setObjectName("F3")
        F3.resize(900, 585)
        F3.setMinimumSize(QtCore.QSize(900, 585))
        F3.setMaximumSize(QtCore.QSize(900, 585))
        F3.setStyleSheet("background-color: rgb(250,250,250)")
        self.OB14 = QtWidgets.QLabel(F3)
        self.OB14.setGeometry(QtCore.QRect(390, 160, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Urdu Typesetting")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.OB14.setFont(font)
        self.OB14.setStyleSheet("background-color: None;\n"
"color: rgb(22, 22, 0);")
        self.OB14.setObjectName("OB14")
        self.OB15 = QtWidgets.QLabel(F3)
        self.OB15.setGeometry(QtCore.QRect(590, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB15.setFont(font)
        self.OB15.setStyleSheet("background-color: None")
        self.OB15.setObjectName("OB15")
        self.OB16 = QtWidgets.QLabel(F3)
        self.OB16.setGeometry(QtCore.QRect(600, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB16.setFont(font)
        self.OB16.setStyleSheet("background-color: None")
        self.OB16.setObjectName("OB16")
        self.OB11 = QtWidgets.QLineEdit(F3)
        self.OB11.setGeometry(QtCore.QRect(380, 280, 181, 31))
        self.OB11.setObjectName("OB11")
        self.OB12 = QtWidgets.QLineEdit(F3)
        self.OB12.setGeometry(QtCore.QRect(380, 340, 181, 31))
        self.OB12.setEchoMode(QtWidgets.QLineEdit.Password)
        self.OB12.setObjectName("OB12")
        self.OB13 = QtWidgets.QLabel(F3)
        self.OB13.setGeometry(QtCore.QRect(0, 0, 900, 585))
        self.OB13.setText("")
        self.OB13.setPixmap(QtGui.QPixmap("scr1.jpg"))
        self.OB13.setScaledContents(True)
        self.OB13.setObjectName("OB13")
        self.OB17 = QtWidgets.QPushButton(F3)
        self.OB17.setGeometry(QtCore.QRect(410, 430, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.OB17.setFont(font)
        self.OB17.setStyleSheet("background-color: rgb(139, 179, 158);\n"
"border-radius:20px")
        self.OB17.setObjectName("OB17")
        self.OB13.raise_()
        self.OB14.raise_()
        self.OB15.raise_()
        self.OB16.raise_()
        self.OB11.raise_()
        self.OB12.raise_()
        self.OB17.raise_()

        self.retranslateUi(F3)
        QtCore.QMetaObject.connectSlotsByName(F3)

    def retranslateUi(self, F3):
        _translate = QtCore.QCoreApplication.translate
        F3.setWindowTitle(_translate("F3", "Form"))
        self.OB14.setText(_translate("F3", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ورود به حساب کاربری</span></p></body></html>"))
        self.OB15.setText(_translate("F3", "<html><head/><body><p align=\"right\">:نام کاربری</p></body></html>"))
        self.OB16.setText(_translate("F3", "<html><head/><body><p align=\"right\">:گذرواژه</p></body></html>"))
        self.OB17.setText(_translate("F3", "ورود"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F3 = QtWidgets.QWidget()
    ui = Ui_F3()
    ui.setupUi(F3)
    F3.show()
    sys.exit(app.exec_())
