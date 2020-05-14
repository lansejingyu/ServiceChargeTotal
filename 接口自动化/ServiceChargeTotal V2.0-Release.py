# -*- coding:utf-8 -*-
# 遵循代码PEP8规范

import requests
import decimal  # 用于十进制数学计算，更接近我们手动计算结果。

# ----------登录，获取token------------
url = "http://api.test.league.xy/league/admin/login"
# payload = {'username': 'admin',
# 		   'password': 'iY10arHx1GQGet8fc3OZzlxKwjcsKPe2XNRKGhhN644='}

payload = {'username': 'admin',
		   'password': 'N5yswN5kdP2zYrIRJv4HiQ=='}

headers = {
	'Content-Type': 'application/x-www-form-urlencoded	'}
response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()["data"]["accessToken"]


# ---------查询订单详情----------------
def KeyValues(response):  # 将重复打印的内容，定义一个函数
	print("运营名称:", json['data']['fskuName'])
	print("SKU编码:", json['data']['fskuCode'])
	print("贸易类型:", json['data']['ftradeTypeName'])
	print("联盟销售单价:", json['data']['fskuSalePrice'])
	print("实际销售单价：", json['data']['fskuPrice'])
	print("数量:", json['data']['fskuNum'])
	print("优惠:", json['data']['skuDiscountAmount'])
	print("实付总额:", json['data']['skuPayAmount'])
	print("佣金费:", json['data']['serviceCharge'])
	print("佣金费单位(1-元，2-百分比):", json['data']['fserviceChargeUnit'])  # 1-元，2-百分比
	Blanklines()
	print("计算佣金费总额中...")


def Blanklines():  # 打印一行空白行，定义一个函数
	print()


def JudgeOrderNo():  # -----从输入联盟订单号~计算完成整个过程，定义一个函数，可重复调用/
	OrderNo = input("请输入要计算的联盟订单号：")

	url = "http://api.test.league.xy/league/order/orderDetail?orderNo=" + OrderNo

	headers = {
		'Content-Type': 'application/json',
		'accessToken': token
	}

	response = requests.request("POST", url=url, headers=headers)

	json = response.json()

	if json['code'] != "200":
		print("服务器错误")
		Blanklines()
		JudgeOrderNo()

	elif json['data'] == {}:
		print("未找到该联盟订单信息")
		Blanklines()
		JudgeOrderNo()

	# 自营社交，佣金非单位为元，且没有优惠
	elif OrderNo == json['data']['fid'] and json['data']['fabbreviationName'] == '自营社交' and \
			json['data']['skuDiscountAmount'] == 0 and json['data']['fserviceChargeUnit'] == 1:
		KeyValues(response)
		# 计算公式  服务费总额：serviceChargeTotal
		serviceChargeTotal = json['data']['fskuNum'] * json['data']['serviceCharge']
		print("服务费总额：", decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()
		JudgeOrderNo()

	# 自营社交，佣金非单位为元，且有优惠
	elif OrderNo == json['data']['fid'] and json['data']['fabbreviationName'] == '自营社交' and \
			json['data']['skuDiscountAmount'] != 0 and json['data']['fserviceChargeUnit'] == 1:
		KeyValues(response)
		# 计算公式  服务费总额：serviceChargeTotal
		serviceChargeTotal = json['data']['skuPayAmount'] * json['data']['serviceCharge'] / \
							 json['data']['fskuSalePrice']
		print("服务费总额：", decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()
		JudgeOrderNo()

	# 自营社交，佣金非单位为%
	elif OrderNo == json['data']['fid'] and json['data']['fabbreviationName'] == '自营社交' and json['data'][
		'fserviceChargeUnit'] == 2:
		KeyValues(response)
		# 计算公式  服务费总额：serviceChargeTotal
		serviceChargeTotal = json['data']['skuPayAmount'] * json['data']['serviceCharge'] / \
							 json['data']['fskuSalePrice']
		print("服务费总额：", decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()
		JudgeOrderNo()

	elif OrderNo == json['data']['fid'] and json['data']['fabbreviationName'] != '自营社交' and json['data']['fserviceChargeUnit'] == 1:
		KeyValues(response)
		# 计算公式  服务费总额：serviceChargeTotal
		serviceChargeTotal = (json['data']['serviceCharge'] - (
				json['data']['fskuSalePrice'] - json['data']['fskuPrice'])) * \
							 json['data']['fskuNum'] - json['data']['skuDiscountAmount']
		print("服务费总额：", decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()
		JudgeOrderNo()

	elif OrderNo == json['data']['fid'] and json['data']['fserviceChargeUnit'] == 2:
		KeyValues(response)
		# 计算公式  服务费总额：serviceChargeTotal
		serviceChargeTotal = json['data']['fskuSalePrice'] * json['data']['fskuNum'] * \
							 json['data']['serviceCharge'] * 0.01 + (
									 json['data']['fskuPrice'] - json['data'][
								 'fskuSalePrice']) * json['data']['fskuNum'] - json['data'][
								 'skuDiscountAmount']
		print("服务费总额：", decimal.Decimal(value=serviceChargeTotal).quantize(exp=decimal.Decimal(value='0.00')))
		Blanklines()
		JudgeOrderNo()


JudgeOrderNo()
