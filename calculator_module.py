def menu ():
    print('_-'*20)
    print('')
    print(f'hello welcome to this calculator \n 1 = darage(1) \n 2= darage(2) \n 3 = shomarande \n 100 = exit ')
    input1=input('please selecte your work:')
    return input1


def f_darage_1():
    a=int(input('please enter a : '))
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
        print('ok your answer is : ', round(x,2))
        
    elif e=='no':
        print('ok')
        print(x)
        


def f_darage_2():
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
            
        elif delta==0:
            x1= (-b /(2*a))
            print(f'x_1: {x1}')
            
        elif delta<0:
            print('it doesnt have rishe')
            

def f_shomarande ():
    user_input=int(input('number you want to get there shomarande: '))
    lst_1=[]    
    for i in range(1,user_input):
        if user_input % i==0:
            user_input=user_input/i
            lst_1.append(user_input)
    print(lst_1)
    



def f_exit():
        print('thank you bye')
        print('_-'*20)
        
        

