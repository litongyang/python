# -*- coding: utf-8 -*-

from openpyxl import Workbook
workbook=Workbook()
sheet1=workbook.active
sheet1.cell(row=5,column=3).value="我喜欢编程"
workbook.save("exercise7_3.xlsx")