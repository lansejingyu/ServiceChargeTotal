# -*- coding:utf-8 -*-
import requests
# from denglu import token
import decimal

url = "http://192.168.2.127:8082/league/admin/login"
payload = {'username': 'admin',
		   'password': 'HGBnGUVR1HvaWkkniwVMvg=='}
files = [

]
headers = {
	'Content-Type': 'application/x-www-form-urlencoded	'
}
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# print(response.text.encode('utf8'))
# print(response.json())
token = response.json()["data"]["accessToken"]
# print(token)


#---------查询订单----------------

orderNo = input("请输入要查询的联盟订单号：")

ip = "http://192.168.2.127:8082/league/order/orderDetail?orderNo="
url = ip + orderNo
# print(url)

payload  = {

        }

headers = {
	'Content-Type': 'application/json',
	'accessToken': token
}

response = requests.request("POST", url=url, headers=headers, data = payload)

# print(response.json())


# skuSalePrice = response.json()['data']['fskuSalePrice']
# skuPrice = response.json()['data']['fskuPrice']
# if	response.json()['code'] != "200" :
# 	print("服务器错误")
#
# elif response.json()['data'] == {}:
# 	print("响应内容为空")
# 	orderNo = input("2重新输入要查询的联盟订单号：")

if orderNo == response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] == 1:
	print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
	print("实际销售单价：",response.json()['data']['fskuPrice'])
	print("数量：",response.json()['data']['fskuNum'])
	print("服务费：",response.json()['data']['serviceCharge'])
	print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
	serviceChargeTotal = response.json()['data']['serviceCharge']-(response.json()['data']['fskuSalePrice'] - response.json()['data']['fskuPrice'])*response.json()['data']['fskuNum']
	print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))


elif orderNo == response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] ==2 and response.json()['data']['fskuPrice'] > response.json()['data']['fskuSalePrice']:
	print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
	print("实际销售单价：",response.json()['data']['fskuPrice'])
	print("数量：",response.json()['data']['fskuNum'])
	print("服务费：",response.json()['data']['serviceCharge'])
	print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
	serviceChargeTotal = response.json()['data']['fskuSalePrice']*response.json()['data']['fskuNum']*response.json()['data']['serviceCharge']*0.01+(response.json()['data']['fskuPrice']-response.json()['data']['fskuSalePrice'])*response.json()['data']['fskuNum']
	print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))


elif orderNo == response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] ==2 and response.json()['data']['fskuPrice'] < response.json()['data']['fskuSalePrice']:
	print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
	print("实际销售单价：",response.json()['data']['fskuPrice'])
	print("数量：",response.json()['data']['fskuNum'])
	print("服务费：",response.json()['data']['serviceCharge'])
	print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
	serviceChargeTotal = response.json()['data']['fskuSalePrice']*response.json()['data']['fskuNum']*response.json()['data']['serviceCharge']*0.01-(response.json()['data']['fskuPrice']-response.json()['data']['fskuSalePrice'])*response.json()['data']['fskuNum']
	print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
else:
	print("计算错误")
