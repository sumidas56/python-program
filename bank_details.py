account={}
name=input("USER NAME")
address=input("ENTER THE ADDRESS")
age=input("USER AGE")
contact=input("CONTACT NUMBER")

account['USERNAME']=name
account['ADDRESS']=address
account['AGE']=age
account['CONTACTNO']=contact
print('Details')

for i,j in account.items():
    print(i, ':', j)

