# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(522, 410)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buildsheet = QtWidgets.QLineEdit(Dialog)
        self.buildsheet.setObjectName("buildsheet")
        self.verticalLayout.addWidget(self.buildsheet)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.testNumber = QtWidgets.QLineEdit(Dialog)
        self.testNumber.setObjectName("testNumber")
        self.verticalLayout.addWidget(self.testNumber)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.qualitySlider = QtWidgets.QSlider(Dialog)
        self.qualitySlider.setSingleStep(5)
        self.qualitySlider.setSliderPosition(80)
        self.qualitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.qualitySlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.qualitySlider.setTickInterval(5)
        self.qualitySlider.setObjectName("qualitySlider")
        self.verticalLayout.addWidget(self.qualitySlider)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.transBox = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transBox.sizePolicy().hasHeightForWidth())
        self.transBox.setSizePolicy(sizePolicy)
        self.transBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transBox.setAutoFillBackground(False)
        self.transBox.setIconSize(QtCore.QSize(26, 16))
        self.transBox.setObjectName("transBox")
        self.verticalLayout.addWidget(self.transBox, 0, QtCore.Qt.AlignHCenter)
        self.pathBtn = QtWidgets.QPushButton(Dialog)
        self.pathBtn.setObjectName("pathBtn")
        self.verticalLayout.addWidget(self.pathBtn)
        self.retranslateUi(Dialog)
        self.qualitySlider.valueChanged['int'].connect(self.label_5.setNum)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pictures To Excel"))
        self.label.setText(_translate("Dialog", "Title"))
        self.label_2.setText(_translate("Dialog", "Number of Tests"))
        self.label_4.setText(_translate("Dialog", "Compression Quality"))
        self.label_5.setText(_translate("Dialog", "80"))
        self.label_3.setText(_translate("Dialog", "Select this to insert pictures column by column"))
        self.transBox.setText(_translate("Dialog", "Transpose"))
        self.pathBtn.setText(_translate("Dialog", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
