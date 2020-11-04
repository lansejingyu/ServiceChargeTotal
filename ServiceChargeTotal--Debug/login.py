import requests

url = "http://api.test.league.xy/league/admin/login"

payload = {'username': 'admin',
		   'password': 'N5yswN5kdP2zYrIRJv4HiQ=='}

files = [

]

headers = {
	'Content-Type': 'application/x-www-form-urlencoded	'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text.encode('utf8'))

# print(response.json())

if response.json()["code"] == "200":
	token = response.json()["data"]["accessToken"]
	# print(token)
else:
	print("登录失败")
