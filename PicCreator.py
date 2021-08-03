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

class PictureApp(QtWidgets.QDialog, Mainwindow.Ui_Dialog):
    def __init__(self,parent=None):
        super(PictureApp, self).__init__(parent)
        self.setupUi(self)
        self.pathBtn.clicked.connect(self.save_pictures)
        self.testNumber.textChanged.connect(self.checker)

        
    def save_pictures(self):
       if self.transBox.isChecked():
           self.pic_by_row()
       else:
           self.pic_by_col()
    def checker(self):
        value = self.testNumber.text()
        try:
            value = int(value)
            self.testNumber.setStyleSheet("QWidget { background-color: #4BF62B}")
        except ValueError:
            self.testNumber.setStyleSheet("QWidget { background-color: #F51B17}")

    def pic_by_row(self):
        directory = []
        picList = []
        quality = self.qualitySlider.value()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"File Directory for Saving")
        title = self.buildsheet.text()
        picWorkbook = Workbook(directory + "/" + title+".xlsx",{'in memory': True})
        worksheet = picWorkbook.add_worksheet('Pictures')
        variable_format = picWorkbook.add_format({'bold':1,'border':1,'align':'center','valign':'vcenter'})
        numTests = self.testNumber.text()
        try:
            numTests = int(numTests)
        except ValueError:
            return
        picList = []

        for i in range(1,numTests+1):
            pictures = QtWidgets.QFileDialog.getOpenFileNames(self,("Select Pictures for # %d" % i))
            picList.append(pictures[0])
            # 10 in Arial excel measurments is 75px so 20 should be 150px

        listSize = 0
        maxlistSize = 0
        for i in picList:
            listSize = len(i)
            if listSize > maxlistSize:
                maxlistSize = listSize
        worksheet.merge_range(0,0,0,maxlistSize+1,title,variable_format)
        worksheet.set_column_pixels(1,maxlistSize+1,175)
        row = 1
        scaled_filepath = []
        pic_count = 0
        for i in picList:
            col = 1
            worksheet.write(row,0,row,variable_format)
            worksheet.set_row_pixels(row,175)
            col += 1
            xoff = 0
            colcount = 1
            for j in i:
                img = Image.open(j)
                filepath, filename = os.path.split(j)
                imgwidth, imgheight = img.size
                scalwidth = imgwidth * (quality/100)
                scalheight = imgheight * (quality/100)
                img = img.resize((int(scalwidth),int(scalheight)),Image.ANTIALIAS)
                scaledname = self.buildsheet.text() +'_' + str(pic_count)
                filepath = filepath+'\\'+scaledname+'_scaled' + '.png'
                img.save(filepath,optimize = True)
                img = Image.open(filepath)
                imgwidth, imgheight = img.size
                if imgwidth > 150:
                    xscale = 150/imgwidth
                    yscale = xscale
                else:
                    xscale = 1
                    yscale = 1
                worksheet.insert_image(row, colcount, filepath,{'x_scale':xscale,'y_scale':yscale})
                xoff += imgwidth * xscale + 1
                scaled_filepath.append(filepath)
                pic_count += 1
                colcount += 1
                img.close()
            row += 1

        picWorkbook.close()
        for i in scaled_filepath:
            os.remove(i)


    def pic_by_col(self):
        directory = []
        picList = []
        quality = self.qualitySlider.value()
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
        for i in range(1, numTests + 1):
            pictures = QtWidgets.QFileDialog.getOpenFileNames(self, ("Select Pictures for # %d" % i))
            picList.append(pictures[0])
            # 10 in Arial excel measurments is 75px so 20 should be 150px
            worksheet.set_column_pixels(1, numTests, 175)
        worksheet.merge_range(0, 0, 0, numTests, title, variable_format)
        col = 1
        scaled_filepath = []
        pic_count = 1
        for i in picList:
            row = 1
            worksheet.write(row, col, col, variable_format)
            row += 1
            for j in i:
                img = Image.open(j)
                filepath, filename = os.path.split(j)
                imgwidth, imgheight = img.size
                scalwidth = imgwidth 
                scalheight = imgheight 
                img = img.resize((int(scalwidth), int(scalheight)), Image.ANTIALIAS)
                scaledname = self.buildsheet.text() + '_' + str(pic_count)
                filepath = filepath + '\\' + scaledname + '_scaled' + '.png'
                img.save(filepath, quality = quality)
                img = Image.open(filepath)
                imgwidth, imgheight = img.size
                if imgwidth > 150:
                    xscale = 150 / imgwidth
                    yscale = xscale
                else:
                    xscale = 1
                    yscale = 1
                worksheet.set_row_pixels(row,175)
                worksheet.insert_image(row, col, filepath, {'x_scale': xscale, 'y_scale': yscale})
                scaled_filepath.append(filepath)
                pic_count += 1
                row += 1
                img.close()
            col += 1

        workbook.close()
        for i in scaled_filepath:
            os.remove(i)
def main():
    app = QtWidgets.QApplication(argv)
    form = PictureApp()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()