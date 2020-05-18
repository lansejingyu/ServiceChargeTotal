import ast
import hashlib

body = input('请输入请求参数:')

# 将输入的字符串转化为字典型dict
dictA = ast.literal_eval(body)
# print(type(dictA))
# 将转换后的字段型字符串，进行字典默认排序
# print(sorted(dictA.items()))  # items为一个字符串  sorted为排序函数

stringA = ""
for i in sorted(dictA):
	# print(i + "=" + str(dictA[i]))
	stringA = stringA + i + "=" + str(dictA[i]) + "&"

# print(stringA + "key=82a9ad9c048a4aa19dffa1c2506cdab4")
stringSignTemp = stringA + "key=82a9ad9c048a4aa19dffa1c2506cdab4"
print(stringSignTemp.lower())  # 全部转小写

sign = hashlib.md5()
sign.update(stringSignTemp.lower().encode(encoding='utf-8'))
print("sign:", sign.hexdigest())