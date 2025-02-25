from math import log2
def solution(y):
    L,R=1,y
    eps=1e-5
    while R-L>=eps:
        x=L+(R-L)/2
        val=x*x+x+1+log2(x)-y
        if val<0:
            L=x
        else:
            R=x
    x=L+(R-L)/2
    print("%.4f"%x)
while True:
	try:
		solution(int(input()))
	except:
		break
	