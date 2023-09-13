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
        Dialog.setEnabled(True)
        Dialog.resize(622, 166)
        self.Star_Button = QtWidgets.QPushButton(Dialog)
        self.Star_Button.setGeometry(QtCore.QRect(50, 80, 91, 31))
        self.Star_Button.setObjectName("Star_Button")
        self.Stop_Button = QtWidgets.QPushButton(Dialog)
        self.Stop_Button.setGeometry(QtCore.QRect(150, 80, 91, 31))
        self.Stop_Button.setObjectName("Stop_Button")
        self.time_input01 = QtWidgets.QSpinBox(Dialog)
        self.time_input01.setEnabled(True)
        self.time_input01.setGeometry(QtCore.QRect(340, 40, 61, 31))
        self.time_input01.setObjectName("time_input01")
        self.time_input02 = QtWidgets.QSpinBox(Dialog)
        self.time_input02.setEnabled(True)
        self.time_input02.setGeometry(QtCore.QRect(410, 40, 61, 31))
        self.time_input02.setObjectName("time_input02")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(340, 20, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.speed_input = QtWidgets.QSpinBox(Dialog)
        self.speed_input.setEnabled(True)
        self.speed_input.setGeometry(QtCore.QRect(50, 40, 81, 31))
        self.speed_input.setMinimum(10)
        self.speed_input.setMaximum(100)
        self.speed_input.setObjectName("speed_input")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(50, 20, 91, 16))
        self.label_6.setObjectName("label_6")
        self.Time_check = QtWidgets.QPushButton(Dialog)
        self.Time_check.setGeometry(QtCore.QRect(480, 40, 91, 31))
        self.Time_check.setObjectName("Time_check")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(490, 20, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(340, 80, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Star_Button.setText(_translate("Dialog", "啟動"))
        self.Stop_Button.setText(_translate("Dialog", "停止"))
        self.label.setText(_translate("Dialog", "直行時間"))
        self.label_2.setText(_translate("Dialog", "轉彎時間"))
        self.label_6.setText(_translate("Dialog", "速度(10~100)"))
        self.Time_check.setText(_translate("Dialog", "開/關計時器"))
        self.label_7.setText(_translate("Dialog", "計時器:關閉"))
        self.label_8.setText(_translate("Dialog", "目前秒數:0秒"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
