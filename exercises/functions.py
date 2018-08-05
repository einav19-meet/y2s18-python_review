
def my_function():
	print('Enter the number')
	x = int(input())
	for i in range(2,x):
		if x % i==0:
			return False
	return True




print(my_function())
