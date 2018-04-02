x = float(input("请输入数字:"))

y = float(input("请输入数字:"))

z = input("请输入+-*/:")
if z == "+":
	print(x+y)
elif z == "-":
	print(x-y)
elif z == "*":
	print(x*y)
elif z == "/":
	print(x/y)
else:
	print("输入错误")

