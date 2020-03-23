import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


option=webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
# option.add_argument('--headless') # 设置option
# option.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
# driver = webdriver.Chrome('D:\\Chrome\\Application\\chromedriver',chrome_options=option)  # 调用带参数的谷歌浏览器

driver =webdriver.Chrome('D:\\Chrome\\Application\\chromedriver')
# driver.implicitly_wait(20)    # 隐性等待，最长等30秒
# driver.maximize_window()   #浏览器最大化


driver.get('http://league-admin.test.xyb2b.com.cn/login')
driver.find_elements_by_class_name('el-input__inner')[0].send_keys('admin')
driver.find_elements_by_class_name('el-input__inner')[1].send_keys('123456')
driver.find_element_by_class_name('el-button').click()


# time.sleep(0.5)    #加等待时间，防止定位不到元素
#打开菜单按钮
try:
	element = WebDriverWait(driver,5).until(
		EC.presence_of_element_located((By.CLASS_NAME,"hamburger-container"))
	)
	element.click()
finally:
	print("打开菜单按钮")
# driver.find_element_by_class_name('hamburger-container').click()
# print("打开菜单按钮")


time.sleep(0.5)
# 打开订单管理
# try:                                                                     #显式等待
# 	element1 = WebDriverWait(driver,5).until(
# 		EC.presence_of_element_located((By.CLASS_NAME,"el-submenu__title"))
# 	)
# 	element1.click()
# finally:
# 	print("打开订单管理")
driver.find_element_by_class_name('el-submenu__title').click()
print("打开订单管理")


time.sleep(0.5)
#打开全部订单列表
# try:
# 	element3 = WebDriverWait(driver,5).until(
# 		EC.presence_of_element_located((By.CLASS_NAME,"el-menu-item"))
# 	)
# 	element3.click()
# finally:
# 	print("打开全部订单列表")
driver.find_elements_by_class_name('el-menu-item')[1].click()
print("打开全部订单列表")


time.sleep(0.5)
#查询订单（联盟订单号）
forder_id = input("请输入要查询的联盟订单号：")
driver.find_elements_by_class_name('el-input__inner')[1].send_keys(forder_id)
driver.find_elements_by_class_name('el-button')[1].click()

time.sleep(1.0)
#进入该订单的详情页
driver.find_elements_by_class_name('goods-mall')[0].click()


time.sleep(1.5)
#定位/打印联盟销售单价
fskusaleprice = driver.find_elements_by_class_name('cell')[13].text
print('联盟销售单价: ',float(fskusaleprice))

#定位/打印实际销售单价
fskuprice = driver.find_elements_by_class_name('cell')[14].text
print('实际销售单价: ',float(fskuprice))

#定位/打印数量
fskunum = driver.find_elements_by_class_name('cell')[15].text
print('数量: ',float(fskunum))

# #定位/打印服务费
fservicecharge = driver.find_elements_by_class_name('cell')[18].text
print('服务费: ',float(fservicecharge[0:4]))

#计算并打印服务费总额
fservicechargetotal = float(fservicecharge[0])-((float(fskusaleprice)-float(fskuprice))*float(fskunum))
print('服务费总额: ',round(fservicechargetotal,3))  #保留两位小数，四舍五入
















# driver.quit()