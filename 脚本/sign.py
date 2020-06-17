import ast
import hashlib

body = input('请输入请求参数:')

# 将输入的字符串转化为字典型dict
dictA = ast.literal_eval(body)

stringA = ""
for i in sorted(dictA):  # sorted将字典进行排序，默认升序排序
	# print(i + "=" + str(dictA[i]))
	stringA = stringA + i + "=" + str(dictA[i]) + "&"

stringSignTemp = stringA + "key=3fd6281724c24b6d9d3cead38ebca966"  # 不同的API商户，需要更换对应的key
print(stringSignTemp.lower())

sign = hashlib.md5()
sign.update(stringSignTemp.lower().encode(encoding='utf-8'))  # stringSignTemp.lower把将要加签的字符串全部转为小写
print("sign:", sign.hexdigest())