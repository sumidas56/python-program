account={}
account_list=[]
choice="y"
while choice=="y" or choice=="Y":
    name=input("USER NAME")
    account["name"]=name
    # address=input("ENTER THE ADDRESS")
    age=input("USER AGE")
    account["age"]=age
    # contact=input("CONTACT NUMBER")
    account_list.append(account.copy())
    choice=input("do you want to continue")
    # if choice=='n'or 'N':
    #     break
print(account_list)
