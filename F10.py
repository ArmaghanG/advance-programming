# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F10.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F10(object):
    def setupUi(self, F10):
        F10.setObjectName("F10")
        F10.resize(900, 585)
        F10.setMinimumSize(QtCore.QSize(900, 585))
        F10.setMaximumSize(QtCore.QSize(900, 585))
        self.O1 = QtWidgets.QLabel(F10)
        self.O1.setGeometry(QtCore.QRect(0, 0, 900, 585))
        self.O1.setText("")
        self.O1.setPixmap(QtGui.QPixmap("../scr2.jpg"))
        self.O1.setScaledContents(True)
        self.O1.setObjectName("O1")
        self.O2 = QtWidgets.QLabel(F10)
        self.O2.setGeometry(QtCore.QRect(360, 20, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Urdu Typesetting")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.O2.setFont(font)
        self.O2.setObjectName("O2")
        self.O3 = QtWidgets.QLabel(F10)
        self.O3.setGeometry(QtCore.QRect(560, 151, 47, 20))
        self.O3.setObjectName("O3")
        self.O4 = QtWidgets.QLabel(F10)
        self.O4.setGeometry(QtCore.QRect(600, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.O4.setFont(font)
        self.O4.setObjectName("O4")
        self.O8 = QtWidgets.QPushButton(F10)
        self.O8.setGeometry(QtCore.QRect(460, 340, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.O8.setFont(font)
        self.O8.setObjectName("O8")
        self.O9 = QtWidgets.QPushButton(F10)
        self.O9.setGeometry(QtCore.QRect(40, 520, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.O9.setFont(font)
        self.O9.setObjectName("O9")
        self.O5 = QtWidgets.QLabel(F10)
        self.O5.setGeometry(QtCore.QRect(600, 220, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.O5.setFont(font)
        self.O5.setObjectName("O5")
        self.O6 = QtWidgets.QLabel(F10)
        self.O6.setGeometry(QtCore.QRect(590, 280, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.O6.setFont(font)
        self.O6.setObjectName("O6")
        self.O7 = QtWidgets.QLineEdit(F10)
        self.O7.setGeometry(QtCore.QRect(460, 285, 113, 20))
        self.O7.setObjectName("O7")

        self.retranslateUi(F10)
        QtCore.QMetaObject.connectSlotsByName(F10)

    def retranslateUi(self, F10):
        _translate = QtCore.QCoreApplication.translate
        F10.setWindowTitle(_translate("F10", "Form"))
        self.O2.setText(_translate("F10", "     کیف پول من"))
        self.O3.setText(_translate("F10", "0"))
        self.O4.setText(_translate("F10", "موجودی حساب:"))
        self.O8.setText(_translate("F10", "پرداخت "))
        self.O9.setText(_translate("F10", "بازگشت به خانه"))
        self.O5.setText(_translate("F10", "شارژ کیف پول:"))
        self.O6.setText(_translate("F10", "مبلغ قابل پرداخت:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F10 = QtWidgets.QWidget()
    ui = Ui_F10()
    ui.setupUi(F10)
    F10.show()
    sys.exit(app.exec_())
