from math import *

def euler(f, xInit,yInit, xFinal, steps):
	deltaX = (xFinal - xInit) / steps
	for i in range(steps):
		k1 = f(xInit, yInit)
		k2 = f(xInit + deltaX, yInit + deltaX * k1);
		k = (k1 + k2) / 2
		xInit = xInit + deltaX
		yInit = yInit + deltaX * k
 	return yInit

f1 = lambda x,y: y
f2 = lambda x,y: 1/x
f3 = lambda x,y: 4/(1+x**2)

def test(teststring,f,a,b,c):
	tries = [10,20,40,80,160]
	tests = [euler(f1,a,b,c, x) for x in tries]
	output = teststring +" testing, 10: {}, 20: {}, 40: {}, 80: {}, 160: {}...\n"
	return(output.format(*tests))


def testall():
	print test("e = y(1)",f1,0,1.0,1.0)
	print test("ln(2) = y(2)",f2,1.0,0.0,2.0)
	print test("pi = y(1)",f3,0.0,0.0,1.0)

testall()
