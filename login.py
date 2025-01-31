count=0
while count<=3:
    username=input("Enter username : ")
    password=input("Enter password : ")
    if username.lower()=='testuser' and password=='Password@123':
        print('Login successful')
    else:
         print("Ivalid credentials")
         count+=1
if count>3:
    print("You've tried more than 3 times try after 2 mins")