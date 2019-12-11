# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:41:47 2018
@author: scott.downard
"""

from PyQt5 import QtWidgets
from sys import argv
import Mainwindow
import os
from xlsxwriter import Workbook
from PIL import Image


class PictureApp(QtWidgets.QMainWindow, Mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PictureApp, self).__init__(parent)
        self.setupUi(self)
        self.pathBtn.clicked.connect(self.savePictures)
        self.testNumber.textChanged.connect(self.checker)
        perclist = list(range(10, 100, 10))
        for i in range(0, len(perclist)):
            perclist[i] = str(perclist[i]) + "%"
        self.comboBox.addItems(perclist)

    def savePictures(self):
        directory = []
        picList = []
        quality = self.comboBox.currentText()
        quality = quality.replace('%', "")
        quality = int(quality)
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "File Directory for Saving")
        title = self.buildsheet.text()
        workbook = Workbook(directory + "/" + title + ".xlsx")
        worksheet = workbook.add_worksheet('Pictures')
        variable_format = workbook.add_format({'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vcenter'})
        numTests = self.testNumber.text()
        try:
            numTests = int(numTests)
        except ValueError:
            return
        picList = []
        worksheet.merge_range(0, 0, 0, numTests, title, variable_format)
        for i in range(1, numTests + 1):
            pictures = QtWidgets.QFileDialog.getOpenFileNames(self, ("Select Pictures for # %d" % i))
            picList.append(pictures[0])
            # 10 in Arial excel measurments is 75px so 20 should be 150px
            worksheet.set_column(1, numTests, 21)
        complete = int(100 / numTests)

        if self.compressBox.isChecked:
            col = 1
            for i in picList:
                row = 1
                worksheet.write(row, col, col, variable_format)
                row += 1
                yoff = 0
                pic_count = 1
                for j in i:
                    img = Image.open(j)
                    filepath, filename = os.path.split(j)
                    imgwidth, imgheight = img.size
                    scalwidth = imgwidth - (imgwidth - (0.20 * imgwidth))
                    scalheight = imgheight - (imgheight - (0.20 * imgheight))
                    img = img.resize((int(scalwidth), int(scalheight)), Image.ANTIALIAS)
                    scaledname = self.buildsheet.text() + '_' + str(col) + str(pic_count)
                    filepath = filepath + '\\' + scaledname + '_scaled' + '.jpg'
                    img.save(filepath, quality=quality)
                    img = Image.open(filepath)
                    imgwidth, imgheight = img.size
                    if imgwidth > 150:
                        xscale = 150 / imgwidth
                        yscale = xscale
                    else:
                        xscale = 1
                        yscale = 1
                    worksheet.insert_image(2, col, filepath, {'x_scale': xscale, 'y_scale': yscale, 'y_offset': yoff})
                    yoff += imgheight * yscale + 1
                    pic_count += 1
                col += 1
                self.progressBar.setValue(complete)
                complete += complete
                if complete > 100:
                    complete = 100
        else:
            col = 1
            for i in picList:
                row = 1
                worksheet.write(row, col, col, variable_format)
                row += 1
                yoff = 0
                pic_count = 1
                for j in i:
                    img = Image.open(j)
                    filepath, filename = os.path.split(j)
                    imgwidth, imgheight = img.size
                    img.save(filepath, quality=99)
                    img = Image.open(j)
                    imgwidth, imgheight = img.size
                    if imgwidth > 150:
                        xscale = 150 / imgwidth
                        yscale = xscale
                    else:
                        xscale = 1
                        yscale = 1
                    worksheet.insert_image(2, col, filepath, {'x_scale': xscale, 'y_scale': yscale, 'y_offset': yoff})
                    yoff += imgheight * yscale + 1
                    pic_count += 1
                col += 1
                self.progressBar.setValue(complete)
                complete += complete
                if complete > 100:
                    complete = 100
        workbook.close()
        if complete != 100:
            complete = complete + (100 - (complete))

    def checker(self):
        value = self.testNumber.text()
        try:
            value = int(value)
            self.testNumber.setStyleSheet("QWidget { background-color: #4BF62B}")
        except ValueError:
            self.testNumber.setStyleSheet("QWidget { background-color: #F51B17}")


def main():
    app = QtWidgets.QApplication(argv)
    form = PictureApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()