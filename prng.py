import random
import math
s = random.randint(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
x = random.randint(1,6)
y = math.floor(((2*x)/3)**3)
o = s*y
print("s =", s)
print("y =", y)
print("o =", o)
p = []
p.append(o)

# for n in p:
	# if n in p:
		# n = o - 1 #? if seed repeats, -1...+2...-3.../-2x...
	# if n not in p:
		# p.append(o)
		# n = o - 1			
# print("p =", p)
# random.shuffle(p)
# m = (random.choice(p))
# print("m =", m * o)
