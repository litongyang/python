# -*- coding: utf-8 -*-
from mitmproxy.http import flow
def request(flow:flow):
	flow.request.headers['X-Forwarded-For']="10.181.90.220"
	if("http://nc.crm.jx.cmcc/public/LoginAction/isBindLogionIp.action?" in flow.request.url):
		flow.request.headers['X-Forwarded-For'] = "10.181.90.220"    
def response(flow:flow):
	url = 'http://10.180.214.106:18080/bp095/initLogin?method=certSaveCRM&phone_no'
	if url in flow.request.url:
		f = open('pinduoduo.js', 'r', encoding="utf-8")
		data = f.read()
		f.close()
		flow.response.set_text(data)