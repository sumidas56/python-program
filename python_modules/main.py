import master

print(''' 
1). print a number pattern
2). print a pyramid pattern
''')
choice=int(input('enter your choice '))

if choice==1:
    number=int(input('enter your number'))
    master.number_pattern(number)
elif choice==2:
    number=int(input('enter your number'))
    master.pyramid_pattern(number)