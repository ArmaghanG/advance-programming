# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F13.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F13(object):
    def setupUi(self, F13):
        F13.setObjectName("F13")
        F13.resize(900, 585)
        F13.setMinimumSize(QtCore.QSize(900, 585))
        F13.setMaximumSize(QtCore.QSize(900, 585))
        self.backg = QtWidgets.QLabel(F13)
        self.backg.setGeometry(QtCore.QRect(0, 0, 900, 585))
        self.backg.setText("")
        self.backg.setPixmap(QtGui.QPixmap("../../../Desktop/Final Project/scr1.jpg"))
        self.backg.setScaledContents(True)
        self.backg.setObjectName("backg")
        self.title = QtWidgets.QLabel(F13)
        self.title.setGeometry(QtCore.QRect(380, 150, 121, 101))
        font = QtGui.QFont()
        font.setFamily("Urdu Typesetting")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.listWidget = QtWidgets.QListWidget(F13)
        self.listWidget.setGeometry(QtCore.QRect(20, 280, 841, 171))
        self.listWidget.setObjectName("listWidget")
        self.sabt = QtWidgets.QPushButton(F13)
        self.sabt.setGeometry(QtCore.QRect(390, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sabt.setFont(font)
        self.sabt.setObjectName("sabt")
        self.return_2 = QtWidgets.QPushButton(F13)
        self.return_2.setGeometry(QtCore.QRect(20, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.return_2.setFont(font)
        self.return_2.setObjectName("return_2")

        self.retranslateUi(F13)
        QtCore.QMetaObject.connectSlotsByName(F13)

    def retranslateUi(self, F13):
        _translate = QtCore.QCoreApplication.translate
        F13.setWindowTitle(_translate("F13", "Form"))
        self.title.setText(_translate("F13", "سبد خرید"))
        self.sabt.setText(_translate("F13", "ثبت و پرداخت"))
        self.return_2.setText(_translate("F13", "بازگشت به خانه"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F13 = QtWidgets.QWidget()
    ui = Ui_F13()
    ui.setupUi(F13)
    F13.show()
    sys.exit(app.exec_())
