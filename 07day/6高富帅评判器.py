height = float(input("请输入身高"))
money = float(input("请输入身价"))
face = float(input("请输入颜值分"))

if height >= 180 and money >= 1000000 and face >= 90:
	print("高富帅")
elif money >=1000000 and face >= 90:
	print("富帅")
elif face >= 90:
	print("帅")
else height =< 160 and money =< 100 and face =< 60:
	print("矮穷矬")
