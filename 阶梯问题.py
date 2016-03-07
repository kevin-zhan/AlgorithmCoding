#递归 f(n) = f(n-1)+f(n-2)
def fun(n):
	if n == 0:
		print "Invalid inpute"
		return 0
	if n==1:
		return 1
	if n==2:
		return 2
	return fun(n-1)+fun(n-2)
#迭代
def count(n):
	if n == 0:
		print "Invalid inpute"
		return 0
	if n==1:
		return 1
	if n==2:
		return 2
	a = 1
	b = 2
	result = 0
	for i in range(3,n+1):
		result = a + b
		a = b
		b = result
	return result

print count(20)
print fun(20)