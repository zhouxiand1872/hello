import random
import time
list=["薛栋炎","刘瑞涛","崔健","张世豪","李鑫","翟宏乐","周肸","韩跃锐"]
print("班级总人数:%d"%len(list))
print("上帝正在挑选天选之子\n")
time.sleep(3)
i = random.randint(0,len(list)-1)
print("呦，你被上帝选中了:------%s"%list[i])
list.pop(i)
j = random.randint(0,len(list)-1)
print("呦，你看着也不错呦------%s\n"%list[j])

k = int(input("如果想查看奖励请继续:\n1继续 0退出\n"))
if k == 1:
	count = random.randint(10,50)
	print("上帝奖励了你们组%d个俯卧撑"%count)
else:
	print("欢迎下次使用")
