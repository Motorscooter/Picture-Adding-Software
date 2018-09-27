# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 2)
        self.testNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.testNumber.setObjectName("testNumber")
        self.gridLayout.addWidget(self.testNumber, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.buildsheet = QtWidgets.QLineEdit(self.centralwidget)
        self.buildsheet.setObjectName("buildsheet")
        self.gridLayout.addWidget(self.buildsheet, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pathBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pathBtn.setObjectName("pathBtn")
        self.gridLayout.addWidget(self.pathBtn, 5, 0, 1, 2)
        self.compressBox = QtWidgets.QCheckBox(self.centralwidget)
        self.compressBox.setObjectName("compressBox")
        self.gridLayout.addWidget(self.compressBox, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Picture Creator"))
        self.label_2.setText(_translate("MainWindow", "Number of Tests"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.pathBtn.setText(_translate("MainWindow", "Start"))
        self.compressBox.setText(_translate("MainWindow", "Compress Images"))

