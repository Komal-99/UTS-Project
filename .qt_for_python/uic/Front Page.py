# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\aaa\OneDrive - The Northcap university\Desktop\UTS\UTS-Project\ui_files\Front Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1408, 920)
        Dialog.setStyleSheet("background-color:rgb(1, 78, 144)\n"
"")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 260, 831, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 36pt \"Times New Roman\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(490, 380, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 36pt \"Times New Roman\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 90, 291, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\Users\\aaa\\OneDrive - The Northcap university\\Desktop\\UTS\\UTS-Project\\ui_files\\../photos/Logo.jpeg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 650, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(200, 217, 231);\n"
"border-radius: 35px;\n"
"border-width: 2opx;\n"
"color: rgb(1, 78, 144);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 650, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(200, 217, 231);\n"
"border-radius: 35px;\n"
"border-width: 2opx;\n"
"color: rgb(1, 78, 144);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"justify\">Predictive Maintenance</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "PREDICTIVE MAINTENANCE"))
        self.label_3.setText(_translate("Dialog", "MODEL"))
        self.pushButton_3.setText(_translate("Dialog", "HELP"))
        self.pushButton.setText(_translate("Dialog", "START"))
