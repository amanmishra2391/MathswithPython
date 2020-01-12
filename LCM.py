def LCM(x,y):
	c=1
	a=2
	while (x!=1 or y!=1):
		if x%a==0 or y%a==0:
			c=c*a
			if x%a==0:
				x=x/a
			if y%a==0:
				y=y/a
		else:
			a=a+1
	return c
