i_accound ="123456"
i_pwd ="123456"
count =1
while True:
	accound = input("请输入账号:")
	pwd = input("请输入密码:")
	if accound == i_accound and pwd == i_pwd:
		print("登陆成功")
		choose_hero = int(input("0-ADC,1-肉,2-法师,3-刺客"))
		if choose_hero == 0:
			print("鲁班")
		elif choose_hero == 1:
			print("亚瑟")
		elif choose_hero == 2:
			print("小乔")
		elif choose_hero == 3:
			print("李白")
		break
	else:
		print("error%d次"%count)
		count+=1
		if count == 4:
			print("账号被封")
			break
