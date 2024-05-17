arr = []
n = int(input("Enter how many elements to a list: "))
for i in range(1, n+1):
    a = int(input(f"Enter element {i}: "))
    arr.append(a)

print("Your list is:", arr)
n = len(arr)

while (1):
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION \n4.DIVISION \n5.EXIT")
    ch = int(input("Enter your choice: "))

    if ch == 1: 
        sum = 0
        for i in range(0,n):
            sum += arr[i]
        print(f"\n The Sum is : {sum} \n")
    elif ch == 2:
        difference = arr[0]
        for i in range(1, n):
            difference -= arr[i]
        print(f"\n The difference is : {difference} \n")
    elif ch == 3:
        val = arr[0] * arr[1]
        try:
            if val == 0:
                print("\n 0 \n")
                print("The first element of the list is 0, so the answer for the total list is also 0 \n")
            else:
                for i in range(2, n):
                    val *= arr[i]
                print(f"\n The product is : {val} \n")
        except:
            pass
    elif ch == 4:
        if n == 2:
            print(f"\n The quotient of {arr[0]} and {arr[1]} is {round(arr[0]/arr[1],2)} \n")
            print(f"\n The remainder of {arr[0]} and {arr[1]} is {round(arr[0]%arr[1],2)} \n")
        else:
            n1 = int(input("Enter numerator : "))
            n2 = int(input("Enter denominator : "))
            
            try:
                if n2 != 0:
                    print("\n")
                    print("Quotient is : ", round(n1/n2, 2))
                    print("\n")
                    print("Remainder is : ", n1 % n2)
                    print("\n")
                else:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print("\nThe denominator can't be zero \n")
    elif ch == 5:
        print("Exiting ...")
        break
    else:
        print("\nInvalid choice\n ")