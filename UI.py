# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 244)
        self.Confirm_Button = QtWidgets.QPushButton(Dialog)
        self.Confirm_Button.setGeometry(QtCore.QRect(380, 50, 91, 31))
        self.Confirm_Button.setObjectName("Confirm_Button")
        self.Star_Button = QtWidgets.QPushButton(Dialog)
        self.Star_Button.setGeometry(QtCore.QRect(280, 200, 91, 31))
        self.Star_Button.setObjectName("Star_Button")
        self.Stop_Button = QtWidgets.QPushButton(Dialog)
        self.Stop_Button.setGeometry(QtCore.QRect(380, 200, 91, 31))
        self.Stop_Button.setObjectName("Stop_Button")
        self.time_input01 = QtWidgets.QSpinBox(Dialog)
        self.time_input01.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.time_input01.setObjectName("time_input01")
        self.time_input02 = QtWidgets.QSpinBox(Dialog)
        self.time_input02.setGeometry(QtCore.QRect(100, 50, 61, 31))
        self.time_input02.setObjectName("time_input02")
        self.time_input03 = QtWidgets.QSpinBox(Dialog)
        self.time_input03.setGeometry(QtCore.QRect(170, 50, 61, 31))
        self.time_input03.setObjectName("time_input03")
        self.time_input04 = QtWidgets.QSpinBox(Dialog)
        self.time_input04.setGeometry(QtCore.QRect(240, 50, 61, 31))
        self.time_input04.setObjectName("time_input04")
        self.time_input05 = QtWidgets.QSpinBox(Dialog)
        self.time_input05.setGeometry(QtCore.QRect(310, 50, 61, 31))
        self.time_input05.setObjectName("time_input05")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 30, 41, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Confirm_Button.setText(_translate("Dialog", "確認設置"))
        self.Star_Button.setText(_translate("Dialog", "啟動"))
        self.Stop_Button.setText(_translate("Dialog", "停止"))
        self.label.setText(_translate("Dialog", "時間01"))
        self.label_2.setText(_translate("Dialog", "時間02"))
        self.label_3.setText(_translate("Dialog", "時間03"))
        self.label_4.setText(_translate("Dialog", "時間04"))
        self.label_5.setText(_translate("Dialog", "時間05"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
