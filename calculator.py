import math
while True:
    print(' please enter your work: \n a= darage 1 \n b= darage 2 \n s= shomarande \n x= exit')
    admin_choice=input()
    if admin_choice=='a':
        a=int(input('please enter a: '))
        if a ==0:
            print('you cant enter 0!!! ')
            while a==0:
                a=int(input('please enter again:'))
        else:
            print('ok')
        b=int(input('please enter b:'))
        x=-b/a
        if (x>=0 or x<=0) and -b%a==0:
            print('your answer is: ',x)  
            exit() 
        elif (x>0 or x<0) and -b%a!=0:
            print(f'ok, but your answer is {x} do you want to round the x?')
        else:
            print('sorry')
            exit()

        e=input()
        if e =='yes':
            print('ok your answer is : ',round(x,2))
        elif e=='no':
            print('ok')
            print(x)
    elif admin_choice=='b':
        a=int(input('please enter a: '))
        while a==0:
            a=int(input('please enter a again: '))
        else: 
            print('ok')
            b=int(input('plase enter b: '))
            c=int(input('please enter c: '))
            delta= (b*b)-4*(a*c)
            if delta >0:
                delta2= math.sqrt(delta)
                x1=(-b+delta2)/(2*a)
                x2=(-b-delta2)/(2*a)
                print(f'x)1 :{x1} and  x)2: {x2}')
                print('_'*20)
            elif delta==0:
                x1= (-b /(2*a))
                print(f'x_1: {x1}')
                print('_'*20)
            elif delta<0:
                print('it doesnt have rishe')
                print('_'*20)
    elif admin_choice=='s':
        user_input=int(input('number you want to get there shomarande: '))
        lst_1=[]    
        for i in range(1,user_input):
            if user_input % i==0:
                user_input=user_input/i
                lst_1.append(user_input)
        print(lst_1)

    elif admin_choice=='x':
        print('thank you bye')
        break
    else:
        print('_'*20)
        print('sorry we dont have this !!!!')
    print(' do you want to continue? \n y= yes \n n= no ')
    admin_choice2=input(':')
    if admin_choice2 =='y':
        print('ok')
        print('_'*20)
    elif admin_choice2=='n:':
        print('thank you bye')

        exit()
    else:   
        print('sorry !!!!')
        print('_'*20)
        