choice='y'
while choice =='Y' or choice =='y':
    age=int(input("enter your age"))
    if age>=18:
        print("you are eligible")
    else:
        print("you are not eligible")  
    choice=input('Do you Want to Continue? ') 
    if choice=='n' or choice=='N':
        break
    else:
        choice='Y'
        print('invalid entry')