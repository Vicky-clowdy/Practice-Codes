a=int(input("How many numbers :  "))
for i in range(0,a):
	val=(i + (i+1))
	print(f"Current number is {i+1} , Previous number is {i} and Sum of {i+1} and {i} is : ",val)
	