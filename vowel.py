num=input("enter a string")
i='aeiou'
for j in num:
    if j in i:
        print("vowel found")
        break
else :
    print("not found")
