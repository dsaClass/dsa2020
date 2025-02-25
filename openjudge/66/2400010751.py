N,K = map(int,input().split())
a = []
for i in range(N):
	a.append(int(float(input())*100))
L,R = 1, max(a)  
best = 0
def cutnumb(L): 
	total = 0
	for i in range(N):
		total += a[i] // L
		
	return total
while L <= R:  
	mid = L + (R - L)//2
	if cutnumb(mid)>=K:
		best = mid 
		L = mid + 1  
	else:
		R = mid - 1  
print("%.2f" % (best/100))
