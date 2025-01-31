n=int(input("Enter a number: "))
flag=0
if n<=1:
    print("Number is prime")
else:
    for i in range(2,int(n)):
        if n%i==0:
            flag=1
            break
    if(flag==1):
        print("Number is not a prime")
    else:
        print("Number is prime")