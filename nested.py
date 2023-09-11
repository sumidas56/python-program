i=input("do you agree to continue")
if i=='y' or i=='Y':
    a=int(input("enter a num"))
    b=int(input("enter a num"))
    c=int(input("enter a num"))
    if a==b==c:
        print("all are equal")
    elif a>=b and a>=c :
        print(" a num is larger",a)
    elif b>=c and b>=a :
        print("num is larger",b)
    else:
        print(" c is larger",c)    
else:
    print(" discontinue")
         