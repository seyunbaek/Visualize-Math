import matplotlib.pyplot as plt

num = 100
def fibonacci(n):
	sequence = []
	a, b = 0,1
	for i in range(n):
		a, b = b, a+b
		sequence.append(b)
	return sequence

def numbered_list(n):
	num_list = []
	for i in range(1,n+1):
		num_list.append(i)
	return num_list

X = numbered_list(num)
Y = fibonacci(num)

plt.style.use('dark_background')
plt.figure(figsize=(16, 9))
plt.axis('on')
plt.plot(X,Y,'.',color='white',markersize=10)
# plt.savefig("Logistic Map.png",dpi=1200)
plt.show()



