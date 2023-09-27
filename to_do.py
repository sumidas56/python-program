choice='y'
a=[]

while choice !='n':
   print(''' 
    To-Do List
    1) insert the task
    2) remove the task 
    3) view the task
    4) exit
''')
   choices=int(input("enter the task"))
   if choices==1:
       b=str(input("enter new task"))
       a.append(b)
   elif choices==2:
       b=str(input("enter the removing task"))
       a.remove(b)
   elif choices==3:
       for i in a:
           print(">>",i)
   elif choices==4:
       print("quit the list")
       break       
   else:
       print("enter the right choice.....")   
   

    
   
    


