password = 'a123456' #先定義正解
i = 3
while True:
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功')
		break
	elif:
		i = i - 1
		input('輸入錯誤 還有', i ,'次機會')
		if i == 0:
			break