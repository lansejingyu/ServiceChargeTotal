import requests

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
print(token)

