while True:

	i =int(input("请输入数字:"))
	o = int(input("请输入数字:"))
	sum = 0 
	if i < o:
		for l in range(i,o+1):
			print(l)
			sum= sum+l
			
		print(sum)
		break
	else:
		print("输入有误")

