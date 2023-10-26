classes={}
std=[]
tchrs=['sumi','sreelekshmi','surya']

def student():
    name=input("name")
    roll_no=input("roll_num")
    age=input("age")
    clas=input("class[5,6,7]")

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
    tchr_name=input("enter the teacher name")
    

    
        

choice='y'
a=[]
while choice !='n':
   print('''
          STUDENT DETAILS:
    
          1): ADD NEW STUDENT
          2): VIEW STUDENT DETAILS
          3): VIEW TEACHERS INCHARGE''')
   choices=int(input("enter the task"))
   if choices==1:
       student()
   elif choices==2:
       std_view()
   elif choices==3:
       tchr()


    

               