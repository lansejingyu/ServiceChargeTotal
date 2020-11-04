import mysql.connector
import decimal  # 用于十进制数学计算

# 1、未使用优惠券： 佣金总额=下单数量 * 佣金费
# 2、使用优惠券： 佣金总额= 实付总额*佣金率
# （佣金率=佣金费/联盟销售单价 ）

mydb = mysql.connector.connect(host='mysql-0.mysql.xy-mysql.svc.cluster.xyops', user='league_test',
							   passwd='league_test', database='league_test')

mycursor = mydb.cursor()

def Blanklines():  # 打印一行空白行，定义一个函数
	print()

def LMOrderNo():
	forder_id = input("请输入联盟订单号：")
	forder_source = "SELECT forder_source FROM t_order WHERE fid = '%s'" % (forder_id)  # 订单来源 1api 2excel 3自营社交'
	mycursor.execute(forder_source)
	forder_source = mycursor.fetchall()  # fetchall() 获取所有数据
	for x in forder_source:
		forder_source = x[0]
		print("订单来源:", forder_source)

	fsku_discount_amount = "SELECT fsku_discount_amount FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 订单优惠总额
	mycursor.execute(fsku_discount_amount)
	fsku_discount_amount = mycursor.fetchall()
	for x in fsku_discount_amount:
		fsku_discount_amount = x[0]
		print("优惠总额:", fsku_discount_amount)

	fsku_num = "SELECT fsku_num FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 订单sku数量
	mycursor.execute(fsku_num)
	fsku_num = mycursor.fetchall()
	for x in fsku_num:
		fsku_num = x[0]
		print("订单sku数量:", fsku_num)

	fservice_charge = "SELECT fservice_charge FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 订单佣金费
	mycursor.execute(fservice_charge)
	fservice_charge = mycursor.fetchall()
	for x in fservice_charge:
		fservice_charge = x[0]
		print("订单佣金费:", fservice_charge)

	fsku_pay_amount = "SELECT fsku_pay_amount FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 订单实付金额
	mycursor.execute(fsku_pay_amount)
	fsku_pay_amount = mycursor.fetchall()
	for x in fsku_pay_amount:
		fsku_pay_amount = x[0]
		print("订单实付总额:", fsku_pay_amount)

	fsku_sale_price = "SELECT fsku_sale_price FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 联盟销售单价
	mycursor.execute(fsku_sale_price)
	fsku_sale_price = mycursor.fetchall()
	for x in fsku_sale_price:
		fsku_sale_price = x[0]
		print("联盟销售单价:", fsku_sale_price)

	fshare_ratio = "SELECT fshare_ratio FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 推手服务费分成比例
	mycursor.execute(fshare_ratio)
	fshare_ratio = mycursor.fetchall()
	for x in fshare_ratio:
		fshare_ratio = x[0] / 10000
		print("推手服务费分成比例:", fshare_ratio)

	fservice_charge_total = "SELECT fservice_charge_total FROM t_order_sku WHERE forder_id = '%s'" % (
		forder_id)  # 导购端服务费总额
	mycursor.execute(fservice_charge_total)
	fservice_charge_total = mycursor.fetchall()
	for x in fservice_charge_total:
		fservice_charge_total = x[0]
		print("导购端服务费总额:", fservice_charge_total)

	fpush_hand_service_charge_total = "SELECT fpush_hand_service_charge_total FROM t_order_sku WHERE forder_id = '%s'" % (
		forder_id)  # 推手服务费总额
	mycursor.execute(fpush_hand_service_charge_total)
	fpush_hand_service_charge_total = mycursor.fetchall()
	for x in fpush_hand_service_charge_total:
		fpush_hand_service_charge_total = x[0]
		print("推手服务费总额:", fpush_hand_service_charge_total)
		Blanklines()

	if forder_source == 3 and fsku_discount_amount == 0:
		# 未使用优惠券
		fpush_hand_service_charge_total_my = fsku_num * fservice_charge * fshare_ratio
		print("计算推手服务费总额:",
			  decimal.Decimal(value=fpush_hand_service_charge_total_my).quantize(exp=decimal.Decimal(value='0')))

		fservice_charge_total_my = fsku_num * fservice_charge * (1 - fshare_ratio)
		print("计算导购端服务费总额:", decimal.Decimal(value=fservice_charge_total_my).quantize(exp=decimal.Decimal(value='0')))

		if fpush_hand_service_charge_total == fpush_hand_service_charge_total_my and fservice_charge_total == fservice_charge_total_my:
			print("pass")
			Blanklines()
			LMOrderNo()
		else:
			print("fail")
			Blanklines()
			LMOrderNo()

	elif forder_source == 3 and fsku_discount_amount != 0:
		# 使用优惠券
		fpush_hand_service_charge_total_my = fsku_pay_amount * (fservice_charge / fsku_sale_price) * fshare_ratio
		print("计算推手服务费总额:",
			  decimal.Decimal(value=fpush_hand_service_charge_total_my).quantize(exp=decimal.Decimal(value='0')))

		fservice_charge_total_my = fsku_pay_amount * (fservice_charge / fsku_sale_price) * (1 - fshare_ratio)
		print("计算导购端服务费总额:", decimal.Decimal(value=fservice_charge_total_my).quantize(exp=decimal.Decimal(value='0')))

		if fpush_hand_service_charge_total == decimal.Decimal(value=fpush_hand_service_charge_total_my).quantize(
				exp=decimal.Decimal(value='0')) and fservice_charge_total == decimal.Decimal(
			value=fservice_charge_total_my).quantize(exp=decimal.Decimal(value='0')):
			print("pass")
			Blanklines()
			LMOrderNo()
		else:
			print("fail")
			Blanklines()
			LMOrderNo()
LMOrderNo()

123