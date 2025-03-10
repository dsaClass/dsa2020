def can_be_popped(s0,s):
	n=len(s0)
	if len(s)!=n:
		return False
	else:
		if n==0:
			return False
		elif n==1:
			if s==s0:
				return True
			else:
				return False
		elif n>=2:	
			x=s[0]
			if x in s0:
				ind_x=s0.index(x)
			else:
				return False
			probe=101
			for i in range(1,n):
				if s[i] in s0:
					
					y=s0.index(s[i])
				else:
					return False
				if y<ind_x and y<probe:
					probe=y
				elif y<ind_x and y>probe:
					return False
			else:
				return can_be_popped(s0[:ind_x]+s0[ind_x+1:],s[1:])
		
s0=input()
while True:
	try:
		s=input()
	
		if can_be_popped(s0,s):
			print('YES')
		else:
			print('NO')
	except EOFError:
		break