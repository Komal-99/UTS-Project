# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jvish\OneDrive\Desktop\UTS-Project\ui_files\PredictiveMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.visualize = QtWidgets.QPushButton(self.centralwidget)
        self.visualize.setGeometry(QtCore.QRect(810, 420, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.visualize.setFont(font)
        self.visualize.setObjectName("visualize")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(460, 360, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.test_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_size_btn.setGeometry(QtCore.QRect(950, 110, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.test_size_btn.setFont(font)
        self.test_size_btn.setObjectName("test_size_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(460, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(770, 480, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.max_iter = QtWidgets.QLineEdit(self.centralwidget)
        self.max_iter.setGeometry(QtCore.QRect(590, 390, 111, 23))
        self.max_iter.setObjectName("max_iter")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(760, 320, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1061, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.predict_val = QtWidgets.QLabel(self.centralwidget)
        self.predict_val.setGeometry(QtCore.QRect(780, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.predict_val.setFont(font)
        self.predict_val.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.predict_val.setStatusTip("")
        self.predict_val.setAutoFillBackground(False)
        self.predict_val.setStyleSheet("color: rgb(83, 255, 71);background-color:rgb(255, 255, 255)")
        self.predict_val.setObjectName("predict_val")
        self.rmse = QtWidgets.QLabel(self.centralwidget)
        self.rmse.setGeometry(QtCore.QRect(670, 180, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.rmse.setFont(font)
        self.rmse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rmse.setText("")
        self.rmse.setObjectName("rmse")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(460, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.multi_class = QtWidgets.QComboBox(self.centralwidget)
        self.multi_class.setGeometry(QtCore.QRect(590, 420, 111, 23))
        self.multi_class.setObjectName("multi_class")
        self.multi_class.addItem("")
        self.multi_class.addItem("")
        self.multi_class.addItem("")
        self.dwnld = QtWidgets.QPushButton(self.centralwidget)
        self.dwnld.setGeometry(QtCore.QRect(700, 210, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.dwnld.setFont(font)
        self.dwnld.setObjectName("dwnld")
        self.Y_combo = QtWidgets.QComboBox(self.centralwidget)
        self.Y_combo.setGeometry(QtCore.QRect(950, 320, 79, 23))
        self.Y_combo.setObjectName("Y_combo")
        self.fit_inter = QtWidgets.QComboBox(self.centralwidget)
        self.fit_inter.setGeometry(QtCore.QRect(590, 330, 111, 23))
        self.fit_inter.setObjectName("fit_inter")
        self.fit_inter.addItem("")
        self.fit_inter.addItem("")
        self.report = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(20, 300, 391, 181))
        self.report.setObjectName("report")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(420, 460, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.train.setFont(font)
        self.train.setObjectName("train")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(480, 180, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.mse = QtWidgets.QLabel(self.centralwidget)
        self.mse.setGeometry(QtCore.QRect(670, 150, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.mse.setFont(font)
        self.mse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mse.setText("")
        self.mse.setObjectName("mse")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(920, 320, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.randomstate = QtWidgets.QLineEdit(self.centralwidget)
        self.randomstate.setGeometry(QtCore.QRect(590, 300, 111, 23))
        self.randomstate.setObjectName("randomstate")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.X_combo = QtWidgets.QComboBox(self.centralwidget)
        self.X_combo.setGeometry(QtCore.QRect(800, 320, 79, 23))
        self.X_combo.setObjectName("X_combo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 580, 91, 31))
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
        self.predict.setGeometry(QtCore.QRect(420, 570, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.predict.setFont(font)
        self.predict.setObjectName("predict")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(480, 120, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(810, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.mae = QtWidgets.QLabel(self.centralwidget)
        self.mae.setGeometry(QtCore.QRect(670, 120, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.mae.setFont(font)
        self.mae.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mae.setText("")
        self.mae.setObjectName("mae")
        self.solver = QtWidgets.QComboBox(self.centralwidget)
        self.solver.setGeometry(QtCore.QRect(590, 360, 111, 23))
        self.solver.setObjectName("solver")
        self.solver.addItem("")
        self.solver.addItem("")
        self.solver.addItem("")
        self.solver.addItem("")
        self.solver.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 530, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.conf_mat = QtWidgets.QPushButton(self.centralwidget)
        self.conf_mat.setGeometry(QtCore.QRect(560, 470, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.conf_mat.setFont(font)
        self.conf_mat.setObjectName("conf_mat")
        self.test_data = QtWidgets.QLineEdit(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(950, 70, 71, 23))
        self.test_data.setObjectName("test_data")
        self.columns = QtWidgets.QListWidget(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(30, 60, 391, 171))
        self.columns.setObjectName("columns")
        self.color_combo = QtWidgets.QComboBox(self.centralwidget)
        self.color_combo.setGeometry(QtCore.QRect(950, 370, 79, 23))
        self.color_combo.setObjectName("color_combo")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(890, 360, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.Z_combo = QtWidgets.QComboBox(self.centralwidget)
        self.Z_combo.setGeometry(QtCore.QRect(800, 370, 79, 23))
        self.Z_combo.setObjectName("Z_combo")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(760, 370, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 70, 81, 31))
        self.label.setObjectName("label")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setGeometry(QtCore.QRect(630, 70, 121, 21))
        self.accuracy.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.accuracy.setText("")
        self.accuracy.setObjectName("accuracy")
        self.list = QtWidgets.QLineEdit(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(250, 520, 471, 31))
        self.list.setText("")
        self.list.setObjectName("list")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(760, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(1, 78, 144);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.split = QtWidgets.QLabel(self.centralwidget)
        self.split.setGeometry(QtCore.QRect(930, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(11)
        self.split.setFont(font)
        self.split.setStyleSheet("color: rgb(1, 78, 144);")
        self.split.setText("")
        self.split.setObjectName("split")
        self.target = QtWidgets.QLabel(self.centralwidget)
        self.target.setGeometry(QtCore.QRect(890, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.target.setFont(font)
        self.target.setObjectName("target")
        self.Failure_Name = QtWidgets.QLabel(self.centralwidget)
        self.Failure_Name.setGeometry(QtCore.QRect(860, 530, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Failure_Name.setFont(font)
        self.Failure_Name.setObjectName("Failure_Name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 26))
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
        self.visualize.setText(_translate("MainWindow", "3-D Plot"))
        self.label_22.setText(_translate("MainWindow", "Solver:"))
        self.test_size_btn.setText(_translate("MainWindow", "Set"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hyper Parameters</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "Fit_intercept:"))
        self.label_9.setText(_translate("MainWindow", "Random State:"))
        self.label_19.setText(_translate("MainWindow", "Predicted "))
        self.max_iter.setText(_translate("MainWindow", "100"))
        self.label_17.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Predictive Maintenance Model</p></body></html>"))
        self.predict_val.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "multi_class:"))
        self.multi_class.setItemText(0, _translate("MainWindow", "auto"))
        self.multi_class.setItemText(1, _translate("MainWindow", "ovr"))
        self.multi_class.setItemText(2, _translate("MainWindow", "multinomial"))
        self.dwnld.setText(_translate("MainWindow", "Download Model"))
        self.fit_inter.setItemText(0, _translate("MainWindow", "True"))
        self.fit_inter.setItemText(1, _translate("MainWindow", "False"))
        self.train.setText(_translate("MainWindow", "Train"))
        self.label_14.setText(_translate("MainWindow", "Root Mean Sq. Error:"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Classification Report:</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Y:"))
        self.label_7.setText(_translate("MainWindow", "Max_Iter:"))
        self.randomstate.setText(_translate("MainWindow", "1.0"))
        self.label_13.setText(_translate("MainWindow", "Mean Square Error:"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.predict.setText(_translate("MainWindow", "Predict"))
        self.label_15.setText(_translate("MainWindow", "Mean Absolute Error:"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Test Train Split</p></body></html>"))
        self.solver.setItemText(0, _translate("MainWindow", "lbfgs"))
        self.solver.setItemText(1, _translate("MainWindow", "liblinear"))
        self.solver.setItemText(2, _translate("MainWindow", "sag"))
        self.solver.setItemText(3, _translate("MainWindow", "saga"))
        self.solver.setItemText(4, _translate("MainWindow", "netwon-cg"))
        self.label_16.setText(_translate("MainWindow", "Enter List for Prediction in [] :"))
        self.conf_mat.setText(_translate("MainWindow", "Confusion Matrix"))
        self.test_data.setText(_translate("MainWindow", "0.1"))
        self.label_20.setText(_translate("MainWindow", "Color:"))
        self.label_24.setText(_translate("MainWindow", "Z:"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Accuracy:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">3-D Scatter Plot</p></body></html>"))
        self.target.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.Failure_Name.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
