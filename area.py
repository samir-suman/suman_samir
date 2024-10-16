print('''choose 1 if u want to find area area of sphere
choose 2 if u want to find the the  perimeter of sphere
choose 3 if u wqant to find the area of squara
choose 4 ifc u weant top find area of reactrangle
choose 5 if u want to find perimeter of square
choose 6 if u want to find perimeter of rectrangle
choose 7 for find area of circle
choose 8 for find perfimeter for circle
choose 9 for find table of any number''')
print("__________________________________________________________________")
a=int(input('enter your choose ='))
if a==1:
    b=float(input('enter the radius='))
    print('this is your answer=',4*3.14*b*b*b)
elif a==2:
    b=float(input('enter the radius='))
    print('this is your answer=',4*3.14*b*b)    
elif a==3:
    b=float(input('enter the length='))
    print('this is your answer=',b*b)
elif a==4:
    b=float(input('enter the length='))
    r=float(input('enter the breath='))
    print('this is your answer=',b*r)
elif a==5:
    b=float(input('enter the length='))
    print('this is your answer',4*b)
elif a==6:
    b=float(input('enter the length='))
    r=float(input('enter the breath='))
    print('this is your answer=',2*(b+r))
elif a==7:
    b=float(input('enter the radius='))
    print('this is your answer=',3.14*b*b)
elif a==8:
    b=float(input('enter the radius='))
    print('this is your answer=',2*3.14*b)
elif a==9:
    a=int(input('the number which u want for table='))
    b=1
    while b<=10:
        print(a,'*',b,'=',a*b)
        b=b+1

else :
    print('faltu ka kaam mat karo ')
