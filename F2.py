# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F2(object):
    def setupUi(self, F2):
        F2.setObjectName("F2")
        F2.resize(900, 585)
        F2.setMinimumSize(QtCore.QSize(900, 585))
        F2.setMaximumSize(QtCore.QSize(900, 585))
        F2.setStyleSheet("background-color: rgb(245, 149, 229);\n"
"background-color: rgb(255, 198, 248);")
        self.OB10 = QtWidgets.QLabel(F2)
        self.OB10.setGeometry(QtCore.QRect(350, 190, 221, 131))
        font = QtGui.QFont()
        font.setFamily("Urdu Typesetting")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.OB10.setFont(font)
        self.OB10.setStyleSheet("background-color: None;")
        self.OB10.setObjectName("OB10")
        self.OB8 = QtWidgets.QPushButton(F2)
        self.OB8.setGeometry(QtCore.QRect(410, 330, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.OB8.setFont(font)
        self.OB8.setStyleSheet("background-color:   rgb(139, 179, 158);\n"
"border-radius:20px")
        self.OB8.setObjectName("OB8")
        self.OB9 = QtWidgets.QPushButton(F2)
        self.OB9.setGeometry(QtCore.QRect(410, 430, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.OB9.setFont(font)
        self.OB9.setStyleSheet("background-color: rgb(139, 179, 158);\n"
"border-radius:20px")
        self.OB9.setObjectName("OB9")
        self.OB7 = QtWidgets.QLabel(F2)
        self.OB7.setEnabled(True)
        self.OB7.setGeometry(QtCore.QRect(0, 0, 900, 585))
        self.OB7.setMouseTracking(False)
        self.OB7.setTabletTracking(False)
        self.OB7.setAutoFillBackground(False)
        self.OB7.setText("")
        self.OB7.setPixmap(QtGui.QPixmap("scr1.jpg"))
        self.OB7.setScaledContents(True)
        self.OB7.setObjectName("OB7")
        self.OB7.raise_()
        self.OB10.raise_()
        self.OB8.raise_()
        self.OB9.raise_()

        self.retranslateUi(F2)
        QtCore.QMetaObject.connectSlotsByName(F2)

    def retranslateUi(self, F2):
        _translate = QtCore.QCoreApplication.translate
        F2.setWindowTitle(_translate("F2", "Form"))
        self.OB10.setText(_translate("F2", "<html><head/><body><p><span style=\" font-size:28pt;\">فروشگاه اینترنتی گل برگ</span></p></body></html>"))
        self.OB8.setText(_translate("F2", "ورود"))
        self.OB9.setText(_translate("F2", "عضویت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F2 = QtWidgets.QWidget()
    ui = Ui_F2()
    ui.setupUi(F2)
    F2.show()
    sys.exit(app.exec_())
