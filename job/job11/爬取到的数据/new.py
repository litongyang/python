# -*- coding: utf-8 -*-
import json
import xlwt
from flask import Flask
from flask import request

workbook = None
sheet = None
cRow = 1
sfile = ""
upload = ""
app = Flask(__name__)
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'

    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ
@app.route('/uploadJson.jsp',methods=["POST"])
def uploadJson():
    if request.method == "POST":
        data = json.loads(request.data.decode('utf-8'))
        saveToFile(data)
        return "success"
@app.route('/initData.jsp')
def initData():
    if(len(upload)>0):
        return upload
    else:
        return "none"
def saveToFile(data):
    global cRow
    if(data['accountname'] == ''):
        print('登录失败')
        sheet.write(cRow, 0, data['account'])
        sheet.write(cRow, 1, "无效用户")
    else:
        sheet.write(cRow, 0, data['account'])
        sheet.write(cRow, 1, data['accountname'])
        sheet.write(cRow, 2, data['real_time_fee'])
        sheet.write(cRow, 3, data['common_fee'])
        sheet.write(cRow, 4, data['plan_name'])
        sheet.write(cRow, 5, data['next_offer_name'])
        sheet.write(cRow, 6, data['accountaddress'])
        sheet.write(cRow, 7, data['wValue'])
        hdname = ""
        hdetime = ""
        for i in data['hdinfo']:
            hdname += i['name'] + "[" +str(i['wvalue']) + "]" + ";"
            hdetime += i['etime'] + ";"
        sheet.write(cRow, 8, hdname)
        sheet.write(cRow, 9, hdetime)
        cx = ""
        for i in data['cxinfo']:
            cx += str(i) + ";"
        sheet.write(cRow, 10, cx)
        sheet.write(cRow, 11, data['login_user_info_user_sts'])
        sheet.write(cRow, 12, data['login_user_info_stop_sts'])
    workbook.save("./" + sfile + ".xls")
    cRow += 1
def init(file):
    global sfile
    sfile = file
    global upload
    try:
        with open("./list.txt",'r' ,encoding="utf-8") as f:
            for l in f.readlines():
                upload += l.strip() + ";"
        global workbook
        global sheet
        workbook = xlwt.Workbook(encoding="utf-8")
        sheet = workbook.add_sheet("sheet")
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold = True
        style.font = font

        sheet.write(0, 0, '账户', style)
        sheet.write(0, 1, '账户名', style)
        sheet.write(0, 2, '实时话费', style)
        sheet.write(0, 3, '余额', style)
        sheet.write(0, 4, '套餐名称', style)
        sheet.write(0, 5, '下周期套餐', style)
        sheet.write(0, 6, '归属地区', style)
        sheet.write(0, 7, '权重值', style)
        sheet.write(0, 8, '活动名称', style)
        sheet.write(0, 9, '失效期时间', style)
        sheet.write(0, 10, '促销信息', style)
        sheet.write(0, 11, '用户状态', style)
        sheet.write(0, 12, '停开机状态', style)
        workbook.save("./" + file + ".xls")
        print("数据初始化成功。。。")
        return True
    except:
        print('数据初始化失败。。。')
        return False
if __name__ == "__main__":
    if(init("爬取到的数据")):
        app.run(host='127.0.0.1',port=9099)
    else:
        pass