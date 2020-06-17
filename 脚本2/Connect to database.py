import mysql.connector

# 1、未使用优惠券： 佣金总额=下单数量 * 佣金费
# 2、使用优惠券： 佣金总额= 实付总额*佣金率
# （佣金率=佣金费/联盟销售单价 ）

mydb = mysql.connector.connect(host='mysql-0.mysql.xy-mysql.svc.cluster.xyops', user='league_test',
							   passwd='league_test', database='league_test')

mycursor = mydb.cursor()

forder_id = input("请输入联盟订单号：")

sql0 = "SELECT fsku_discount_amount FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)  # 订单优惠总额
sql1 = "SELECT fsku_num * fservice_charge FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)
sql2 = "SELECT fshould_server_total_amount FROM t_order_sku WHERE forder_id = '%s'" % (forder_id)
sql3 = "SELECT fsku_pay_amount * fservice_charge / fsku_sale_price FROM t_order_sku WHERE forder_id = '%s'" % (
	forder_id)

mycursor.execute(sql0)
fsku_discount_amount = mycursor.fetchall()
print("订单优惠总额:",fsku_discount_amount)

if fsku_discount_amount == [(0,)]:
	# 未使用优惠券
	mycursor.execute(sql1)
	serviceChargeTotal = mycursor.fetchall()  # fetchall() 获取所有数据
	print("订单佣金费总额:", serviceChargeTotal)

	mycursor.execute(sql2)
	fshould_server_total_amount = mycursor.fetchall()  # fetchall() 获取所有数据
	print("应结算服务费总金额:", fshould_server_total_amount)

	if serviceChargeTotal == fshould_server_total_amount:
		print("通过")
	else:
		print("不通过")

else:
	# 使用优惠券
	mycursor.execute(sql3)
	serviceChargeTotal = mycursor.fetchall()  # fetchall() 获取所有数据
	print("订单佣金费总额:", serviceChargeTotal)

	mycursor.execute(sql2)
	fshould_server_total_amount = mycursor.fetchall()  # fetchall() 获取所有数据
	print("应结算服务费总金额:", fshould_server_total_amount)

	if serviceChargeTotal == fshould_server_total_amount:
		print("通过")
	else:
		print("不通过")
