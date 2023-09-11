a=int(input("enter a number"))
b=int(input("enter a num"))
c=int(input("enter a num"))
if a==b and b==c:
    print("both are equal")
elif a>=b and a>=c:
    print("a is greater")
elif b>=c and b>=a:
    print("b is greater")
else :
    print("c is greater")