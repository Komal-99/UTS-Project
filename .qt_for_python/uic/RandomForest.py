# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\aaa\OneDrive - The Northcap university\Desktop\UTS\UTS-Project\ui_files\RandomForest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 470, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 110, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.bootstrap = QtWidgets.QComboBox(self.centralwidget)
        self.bootstrap.setGeometry(QtCore.QRect(580, 470, 111, 23))
        self.bootstrap.setObjectName("bootstrap")
        self.bootstrap.addItem("")
        self.bootstrap.addItem("")
        self.mse = QtWidgets.QLabel(self.centralwidget)
        self.mse.setGeometry(QtCore.QRect(620, 140, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.mse.setFont(font)
        self.mse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mse.setText("")
        self.mse.setObjectName("mse")
        self.test_data = QtWidgets.QLineEdit(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(900, 60, 71, 23))
        self.test_data.setObjectName("test_data")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(430, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.mae = QtWidgets.QLabel(self.centralwidget)
        self.mae.setGeometry(QtCore.QRect(620, 110, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.mae.setFont(font)
        self.mae.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mae.setText("")
        self.mae.setObjectName("mae")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(710, 270, 20, 251))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 380, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(500, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.train.setFont(font)
        self.train.setObjectName("train")
        self.rmse = QtWidgets.QLabel(self.centralwidget)
        self.rmse.setGeometry(QtCore.QRect(620, 170, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.rmse.setFont(font)
        self.rmse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rmse.setText("")
        self.rmse.setObjectName("rmse")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(430, 440, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(430, 140, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.dwnld = QtWidgets.QPushButton(self.centralwidget)
        self.dwnld.setGeometry(QtCore.QRect(650, 200, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.dwnld.setFont(font)
        self.dwnld.setObjectName("dwnld")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(440, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(430, 170, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setGeometry(QtCore.QRect(580, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.accuracy.setFont(font)
        self.accuracy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.accuracy.setText("")
        self.accuracy.setObjectName("accuracy")
        self.estimators = QtWidgets.QLineEdit(self.centralwidget)
        self.estimators.setGeometry(QtCore.QRect(580, 350, 111, 23))
        self.estimators.setObjectName("estimators")
        self.conf_mat = QtWidgets.QPushButton(self.centralwidget)
        self.conf_mat.setGeometry(QtCore.QRect(750, 340, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.conf_mat.setFont(font)
        self.conf_mat.setObjectName("conf_mat")
        self.criterion = QtWidgets.QComboBox(self.centralwidget)
        self.criterion.setGeometry(QtCore.QRect(580, 380, 111, 23))
        self.criterion.setObjectName("criterion")
        self.criterion.addItem("")
        self.criterion.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(760, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.min_sample_split = QtWidgets.QLineEdit(self.centralwidget)
        self.min_sample_split.setGeometry(QtCore.QRect(580, 440, 111, 23))
        self.min_sample_split.setObjectName("min_sample_split")
        self.test_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_size_btn.setGeometry(QtCore.QRect(900, 100, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.test_size_btn.setFont(font)
        self.test_size_btn.setObjectName("test_size_btn")
        self.max_depth = QtWidgets.QLineEdit(self.centralwidget)
        self.max_depth.setGeometry(QtCore.QRect(580, 410, 111, 23))
        self.max_depth.setObjectName("max_depth")
        self.report = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(10, 290, 391, 171))
        self.report.setObjectName("report")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1001, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.columns = QtWidgets.QListWidget(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(10, 60, 391, 181))
        self.columns.setObjectName("columns")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.randomstate = QtWidgets.QLineEdit(self.centralwidget)
        self.randomstate.setGeometry(QtCore.QRect(580, 320, 111, 23))
        self.randomstate.setObjectName("randomstate")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 550, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.predict_val = QtWidgets.QLabel(self.centralwidget)
        self.predict_val.setGeometry(QtCore.QRect(750, 490, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.predict_val.setFont(font)
        self.predict_val.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.predict_val.setStatusTip("")
        self.predict_val.setAutoFillBackground(False)
        self.predict_val.setStyleSheet("color: rgb(83, 255, 71);\n"
"background-color: rgb(255, 255, 255);")
        self.predict_val.setObjectName("predict_val")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 630, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(430, 590, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.predict.setFont(font)
        self.predict.setObjectName("predict")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(760, 440, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.list = QtWidgets.QLineEdit(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(220, 550, 521, 31))
        self.list.setObjectName("list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_21.setText(_translate("MainWindow", "bootstrap:"))
        self.label_13.setText(_translate("MainWindow", "Mean Absolute Error:"))
        self.bootstrap.setItemText(0, _translate("MainWindow", "True"))
        self.bootstrap.setItemText(1, _translate("MainWindow", "False"))
        self.test_data.setText(_translate("MainWindow", "0.1"))
        self.label_20.setText(_translate("MainWindow", "max_depth:"))
        self.label_3.setText(_translate("MainWindow", "Criterion:"))
        self.train.setText(_translate("MainWindow", "Train"))
        self.label_19.setText(_translate("MainWindow", "min_sample_split:"))
        self.label_15.setText(_translate("MainWindow", "Mean Square Error:"))
        self.dwnld.setText(_translate("MainWindow", "Download"))
        self.label_24.setText(_translate("MainWindow", "Accuracy Score:"))
        self.label_14.setText(_translate("MainWindow", "Root Mean Sq. Error:"))
        self.estimators.setText(_translate("MainWindow", "100"))
        self.conf_mat.setText(_translate("MainWindow", "Confusion Matrix"))
        self.criterion.setItemText(0, _translate("MainWindow", "gini"))
        self.criterion.setItemText(1, _translate("MainWindow", "entropy"))
        self.label_12.setText(_translate("MainWindow", "Test Train Split"))
        self.label_2.setText(_translate("MainWindow", "N_Estimators"))
        self.min_sample_split.setText(_translate("MainWindow", "2"))
        self.test_size_btn.setText(_translate("MainWindow", "Set"))
        self.max_depth.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Random Forest Model</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Classification Report:</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hyper Parameters</p></body></html>"))
        self.randomstate.setText(_translate("MainWindow", "144"))
        self.label_9.setText(_translate("MainWindow", "Random State:"))
        self.label_16.setText(_translate("MainWindow", "Enter List for Prediction :"))
        self.predict_val.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.predict.setText(_translate("MainWindow", "Predict"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Predicted Value</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Visualization</p></body></html>"))
