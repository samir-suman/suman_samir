print(''' if u want ṭo print a equilatetral triangle press ,1 \n if u want to print left side triange press       ,2 \n if u wnnt to print right side triangle press     ,3 \n if u want to print a rectriangle then press      ,4 \n if u want to print square then press             ,5 \n if u want to print circle press                  ,6''')
def pattern():
    r=input ("By which symbol u want to prin your pattern=")
    def equilateral_triangle():
        for i in range (x):
            print(" "*(x-i),((i*2)-1)*r)
    def left_righttriangle():
        for i in range (x):
            print(i*r)
    def right_righttriangle():
        for i in range (x+1):
            print((x-i)*" ",i*r)
    def rectrangle():
        for i in range(x):
            print(r*(x+3))
    def upward_rectrangle():
        if x%2==0:
            print(x//2*r)
        else:
            print(r*((x-1)//2))
    def downward_rectrangle():
        print(r*x*2)
    def circle():
        for i in range(x):
            if x%2==0:
                print(" "*(((x)//2)-2*i),r," "*(((x)//2)+2*i),r)
            else:
                print(" "*(((x+1)//2)-2*i),r," "*(((x+1)//2)-2*i),r)
    a=int(input("enter the choice ="))
    x=int(input("enter no of line for pattern ="))
    if a==1:
        equilateral_triangle()
    elif a==2:
        left_righttriangle()
    elif a==3:
        right_righttriangle()
    elif a==4:
        print("if u want up ward rectrangle press 1 \n if u want to downward rectrangle,2")
        c=int (input("enter what type of rectrangle u want to print="))
        if c==1:
            upward_rectrangle()
        elif c==2:
            downward_rectrangle()
        else :
            print ("wrong selection")
    elif a==6:
        circle()

    else:
        print("wrong choice")
    c=input("if u wamt to run again this program then press (y) \n if not then press (N)")
    if c=="y":
        pattern()
    else :
        print
pattern()
