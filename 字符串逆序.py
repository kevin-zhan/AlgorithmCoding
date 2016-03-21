#coding=utf8
def reverseString(sstr):
	words = sstr.split()
	stackA = ""	
	for i in range(0,len(words)):
		stackA += words.pop() + " "
	print stackA

sss = "I am very happy today"
reverseString(sss)
