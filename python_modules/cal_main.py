import cal_python
print(''' 
1). sum of the digits
2). differnce b/w the digits
3). product of the digits
4).power of the digit
''')
      
choice=int(input("enter your choice"))
if choice==1:
   a=int(input("enter a digit"))
   b=int(input("enter a digit"))
   cal_python.addition(a,b)

elif choice==2:
   a=int(input("enter a digit"))
   b=int(input("enter a digit"))
   cal_python.sub(a,b)

elif choice==3:
   a=int(input("enter a digit"))
   b=int(input("enter a digit"))
   cal_python.product(a,b)

elif choice==4:
    a=int(input("enter a digit"))
    b=int(input("enter a digit"))
    cal_python.power(a,b)

else:
   print("wrong choice...enter the above choice shown ")