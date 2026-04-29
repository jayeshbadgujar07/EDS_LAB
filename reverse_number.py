n=int(input()) #input
reverse =0  #initialize
while n>0: #condition
	d=n%10
	reverse=reverse*10+d
	n=n// 10
print(reverse)