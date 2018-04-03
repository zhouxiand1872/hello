q = 0 
w = 0
while q < 99:
	q+=1
	if q%2 == 0:
		w-=q
	else:
		w+=q
print(w)
