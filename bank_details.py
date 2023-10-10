account={}
account_list=[]
acc_num=1000
def create_account():
    global acc_num
    name=input("USER NAME")
    address=input("ENTER THE ADDRESS")
    age=input("USER AGE")
    contact=input("CONTACT NUMBER")
    acc_bal=0

    account['USERNAME']=name
    account['ACCOUNT NO']=acc_num
    account['ADDRESS']=address
    account['AGE']=age
    account['acc_bal']=acc_bal
    account['CONTACTNO']=contact
    account_list.append(account.copy())
    acc_num+=1

def account_details():
    print("accounts is as follows")
    for account in account_list:
            for i,j in account.items():
                print(i, ':', j)

def account_bal():
    b=int(input("ENTER YOUR accnum"))
    amount=int(input("ENTER YOUR AMOUNT"))
    account1=account_list.copy()
    acc_number=[]
    for i in account1:
        acc_number.append(i['ACCOUNT NO'])
    acc_number.append(i['ACCOUNT NO'])
        
    if  b in acc_number:
        
        for i in account1:
            if i['ACCOUNT NO']==b:
                acc_bal=i['acc_bal']           
                i.update({"acc_bal":acc_bal+amount})


        for account in account1:
            for y,x in account.items():
                print(y,':',x)

def account_withdraw():
    b=int(input("ENTER YOUR accnum"))
    
    account1=account_list.copy()
    acc_number=[]
    for i in account1:
       acc_number.append(i['ACCOUNT NO'])
    if  b in acc_number:
     wid_amount=int(input("enter amount of withdraw"))
    for i in account1:
        if i['ACCOUNT NO']==b:
            acc_bal=i['acc_bal'] 
            if acc_bal>0:
               if acc_bal<wid_amount:
                  print("insufficent balance")
                  break
               else:
                  i.update({'acc_bal':acc_bal-wid_amount})
        else:
            print("acc num not found")
            break
        for account in account1:
            for y,x in account.items():
                print(y,':',x)

choice='y'
a=[]
while choice !='n':
   print(''' 
    BANK_)ACCOUNT
    1) CREATE A NEW ACCOUNT
    2) VIEW  ACCOUNT DETAILS 
    3) CHECK ACC_BALANCE
    4) WIDRAWAL DETAILS
    5) EXIT''')
   choices=int(input("enter the task"))
   if choices==1:
       create_account()
      
   elif choices==2:
       account_details()
      
   elif choices==3:
       account_bal()

   elif choices==4:
       account_withdraw()
           
   elif choices==5:
       break
       
              
   else:
       print("enter the right choice.....")   
   