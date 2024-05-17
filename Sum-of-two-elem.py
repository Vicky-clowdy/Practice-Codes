arr=[]
n=int(input("Enter number of elements to add in list : "))
for i in range(1,n+1):
	a=int(input(f"Enter element {i} : "))
	arr.append(a)
print("Your list is : ",arr)
n=len(arr)
def sortt(arr):
	    for i in range(0,n-1):
        	for j in range(0,n-1):
          	  if(arr[j]>arr[j+1]):
                	arr[j],arr[j+1]=arr[j+1],arr[j]
	    return arr              
sortt(arr)    
print("After sorting : ",arr)   
tar=int(input("Enter sum value of two elements in list : "))         	
left=0
right=n-1
while(left<=right):
	val=arr[left]+arr[right]
	if(val==tar):
		print(f"Value {left} and {right} ")
		break
	elif(val<tar):
		left=left+1
	else:
		right=right-1
