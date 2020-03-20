# -*- coding:utf-8 -*-
import requests
# from denglu import token
import decimal  #用于十进制数学计算，更接近我们计算结果。



#----------登录，获取token------------
url = "http://192.168.2.127:8082/league/admin/login"
payload = {'username': 'admin',
		   'password': 'HGBnGUVR1HvaWkkniwVMvg=='}

headers = {
	'Content-Type': 'application/x-www-form-urlencoded	'
}

response = requests.request("POST", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
# print(response.json())
token = response.json()["data"]["accessToken"]
# print(token)


#---------查询订单----------------
def KeyValues(response):
	print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
	print("实际销售单价：",response.json()['data']['fskuPrice'])
	print("数量：",response.json()['data']['fskuNum'])
	print("服务费：",response.json()['data']['serviceCharge'])
	print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比

def Blanklines():     #打印一行空白行
	print()


def JudgeOrderNo():                                #-----从输入联盟订单号~计算完成整个过程，定义一个函数，可重复调用/
	OrderNo = input("请输入要计算的联盟订单号：")
	url = "http://192.168.2.127:8082/league/order/orderDetail?orderNo=" + OrderNo
	# print(url)

	headers = {
		'Content-Type': 'application/json',
		'accessToken': token
	}

	response = requests.request("POST", url=url, headers=headers)


	if	response.json()['code'] != "200" :
		print("服务器错误")
		Blanklines()   #打印一行空白行
		JudgeOrderNo()

	elif response.json()['data'] == {}:
		print("响应内容为空")
		Blanklines()
		JudgeOrderNo()

	elif OrderNo== response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] == 1:
		# print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
		# print("实际销售单价：",response.json()['data']['fskuPrice'])
		# print("数量：",response.json()['data']['fskuNum'])
		# print("服务费：",response.json()['data']['serviceCharge'])
		# print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
		KeyValues(response)
		serviceChargeTotal = response.json()['data']['serviceCharge']-(response.json()['data']['fskuSalePrice'] - response.json()['data']['fskuPrice'])*response.json()['data']['fskuNum']
		print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()

		JudgeOrderNo()

	elif OrderNo == response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] ==2 and response.json()['data']['fskuPrice'] > response.json()['data']['fskuSalePrice']:
		# print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
		# print("实际销售单价：",response.json()['data']['fskuPrice'])
		# print("数量：",response.json()['data']['fskuNum'])
		# print("服务费：",response.json()['data']['serviceCharge'])
		# print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
		KeyValues(response)
		serviceChargeTotal = response.json()['data']['fskuSalePrice']*response.json()['data']['fskuNum']*response.json()['data']['serviceCharge']*0.01+(response.json()['data']['fskuPrice']-response.json()['data']['fskuSalePrice'])*response.json()['data']['fskuNum']
		print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()

		JudgeOrderNo()

	elif OrderNo == response.json()['data']['fid'] and response.json()['data']['fserviceChargeUnit'] ==2 and response.json()['data']['fskuPrice'] < response.json()['data']['fskuSalePrice']:
		# print("联盟销售单价:",response.json()['data']['fskuSalePrice'])
		# print("实际销售单价：",response.json()['data']['fskuPrice'])
		# print("数量：",response.json()['data']['fskuNum'])
		# print("服务费：",response.json()['data']['serviceCharge'])
		# print("服务费单位(1-元，2-百分比)：",response.json()['data']['fserviceChargeUnit'])  #1-元，2-百分比
		KeyValues(response)
		serviceChargeTotal = response.json()['data']['fskuSalePrice']*response.json()['data']['fskuNum']*response.json()['data']['serviceCharge']*0.01-(response.json()['data']['fskuPrice']-response.json()['data']['fskuSalePrice'])*response.json()['data']['fskuNum']
		print("服务费总额：",decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()

		JudgeOrderNo()

JudgeOrderNo()