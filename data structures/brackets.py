
from collections import deque 
'''
inp: ((()))
out: valid

inp: [(]
out: invalid

inp: (({{[[]]}}))
valid

{gggg(g)))}
invalid

("()")
valid

"((((((({}[][]))))))"

valid

'''

def vaild(x):
	stack = []
	for y in range(len(x)):
		stack.append(x[y])

	y=0
	a=0
	b=0
	k=0
	d=0
	f=0
	n=0
	m=0
	for y in range(len(x)):
		if stack:
			c=stack.pop()
	   
			if c=="(" :
				a+=1
				y+=1  
			elif  c==")":
			   b+=1
			   y+=1
			
			else:
			   
				if c=="[":
				 d+=1
				 y+=1
				elif c=="]":
					f+=1
					y+=1
				else: 
					if c=="{":
						n+=1
						y+=1
					elif c=="}":
						m+=1
						y+=1
					else:
						if c == '"':
							k+=1
							y+=1
		   
			
		if a==b and y==len(x):
		  return True
		elif d==f and y==len(x):
			return True
		elif m==n and y==len(x):
		  return True
		elif k%2==0 and y==len(x):
			return True            
	return False




inp = '''{}{}{}[[[[["]"]]]]'''
assert True == vaild(inp)


inp = '''[["]"]]]]'''
assert True == vaild(inp)
