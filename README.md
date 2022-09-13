# ServiceChargeTotal----行云联盟总服务费计算

！！将脚本转化成可执行程序 .exe 文件  
1.使用pip安装PyInstaller库  
pip install pyinstaller

2.CMD进入目的.py文件夹目录，输入以下代码将.py文件转换成.exe文件  
pyinstaller -F C:\Users\ly\hello.py（文件路径）

3.待命令运行完后，目的.py文件路径下会生成一个dist文件夹，该文件夹里会生成一个与目的.py文件同名的.exe文件。

！！代码逻辑  
1.使用登录接口，获取到用户登录accessToken，定义为token，方便后面的接口使用；  
2.使用联盟订单详情查询接口，获取服务费总额用到的相关字段值；  
3.使用条件判断语句，编写服务费单位不同情况下的服务费总额计算公式；  
4.联盟订单详情查询接口中添加了访问时“服务器错误”及联盟订单号不正确时“响应为空”的判断，可重新输入联盟订单号。