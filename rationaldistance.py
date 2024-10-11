#!/usr/bin/env python3
import math, random
def rational_dist():
	a=(200,200)
	b=(200,-200)
	c=(-200,-200)
	d=(-200,200)
	p=(random.randint(-999999999999999,99999999999999),random.randint(-999999999999999,99999999999999))
	while p:
		v=math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )
		w=math.sqrt( ((p[0]-a[0])**2)+((p[1]-a[1])**2) )
		x=math.sqrt( ((p[0]-b[0])**2)+((p[1]-b[1])**2) )
		y=math.sqrt( ((p[0]-c[0])**2)+((p[1]-c[1])**2) )
		z=math.sqrt( ((p[0]-d[0])**2)+((p[1]-d[1])**2) )
		if w%1==0 and x%1==0 and y%1==0 and z%1==0:
			print(v,w,x,y,z)
			print(p)
			break
		else:
			continue
rational_dist()
'''
f=math.sqrt(2)
g=math.sqrt(2)
while f:
	if b%1==0:
		print(b)
		break
	else:
		b=b+a
		continue
res=173062828
'''
