classes={}
std=[]
tchrs=['sumi','sreelekshmi','surya','krishna','arya','nandana']

def student():
    name=input("name")
    roll_no=input("roll_num")
    age=input("age")
    clas=int(input("class"))
    if clas>=5 and clas<=10:
     print(clas)
    else:
      print("invalid entry")


    classes['name']=name
    classes['roll_no']=roll_no
    classes['age']=age
    classes['clas']=clas

    std.append(classes.copy())

def std_view():
    print("student details")
    for classes in std:
        for i,j in classes.items():
            print(i, ':', j)


def tchr():
    for i in tchrs:
        print(i)

def assign_tchr():
    tchr_name=int(input("select the teacher from the list above"))
    a=tchr_name-1
    print(tchrs[a])
    

    
        

choice='y'
a=[]
while choice !='n':
   print('''
          STUDENT DETAILS:
    
          1): ADD NEW STUDENT
          2): VIEW STUDENT DETAILS
          3): VIEW TEACHERS INCHARGE
          4): SELECT TEACHER''')
   choices=int(input("enter the task"))
   if choices==1:
       student()
   elif choices==2:
       std_view()
   elif choices==3:
       tchr()
   elif choices==4:
       assign_tchr()


    

               