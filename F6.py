# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F6.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_F6(object):
    def setupUi(self, F6):
        F6.setObjectName("F6")
        F6.resize(900, 585)
        F6.setMinimumSize(QtCore.QSize(900, 585))
        F6.setMaximumSize(QtCore.QSize(900, 585))
        self.OB38 = QtWidgets.QLabel(F6)
        self.OB38.setGeometry(QtCore.QRect(0, 0, 900, 585))
        self.OB38.setText("")
        self.OB38.setPixmap(QtGui.QPixmap("scr1.jpg"))
        self.OB38.setScaledContents(True)
        self.OB38.setObjectName("OB38")
        self.OB40 = QtWidgets.QPushButton(F6)
        self.OB40.setGeometry(QtCore.QRect(820, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB40.setFont(font)
        self.OB40.setObjectName("OB40")
        self.OB41 = QtWidgets.QPushButton(F6)
        self.OB41.setGeometry(QtCore.QRect(795, 230, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB41.setFont(font)
        self.OB41.setObjectName("OB41")
        self.OB42 = QtWidgets.QPushButton(F6)
        self.OB42.setGeometry(QtCore.QRect(410, 180, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB42.setFont(font)
        self.OB42.setObjectName("OB42")
        self.OB43 = QtWidgets.QPushButton(F6)
        self.OB43.setGeometry(QtCore.QRect(660, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB43.setFont(font)
        self.OB43.setObjectName("OB43")
        self.OB44 = QtWidgets.QPushButton(F6)
        self.OB44.setGeometry(QtCore.QRect(130, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB44.setFont(font)
        self.OB44.setObjectName("OB44")
        self.OB45 = QtWidgets.QPushButton(F6)
        self.OB45.setGeometry(QtCore.QRect(40, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OB45.setFont(font)
        self.OB45.setObjectName("OB45")
        self.OB39 = QtWidgets.QLabel(F6)
        self.OB39.setGeometry(QtCore.QRect(740, 230, 41, 31))
        self.OB39.setStyleSheet("\n"
"background-color: rgb(218, 218, 218);\n"
"border-radius:40px")
        self.OB39.setObjectName("OB39")

        self.retranslateUi(F6)
        QtCore.QMetaObject.connectSlotsByName(F6)

    def retranslateUi(self, F6):
        _translate = QtCore.QCoreApplication.translate
        F6.setWindowTitle(_translate("F6", "Form"))
        self.OB40.setText(_translate("F6", "خانه"))
        self.OB41.setText(_translate("F6", ":امتیاز من"))
        self.OB42.setText(_translate("F6", "ثبت محصول جدید/شارژمجدد محصولات"))
        self.OB43.setText(_translate("F6", "لیست محصولات موجود من"))
        self.OB44.setText(_translate("F6", "کیف پول من"))
        self.OB45.setText(_translate("F6", "خروج از حساب"))
        self.OB39.setText(_translate("F6", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    F6 = QtWidgets.QWidget()
    ui = Ui_F6()
    ui.setupUi(F6)
    F6.show()
    sys.exit(app.exec_())
