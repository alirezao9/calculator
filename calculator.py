import calculator_module
while True:
    x=calculator_module.menu()
    if x =='1' or x == 1 : 
        calculator_module.f_darage_1()
    elif x =='2' or x == 2 : 
        calculator_module.f_darage_2()
    elif x =='3' or x == 3 : 
        calculator_module.f_shomarande()
    elif x =='100' or x ==100 : 
        calculator_module.f_exit()
        break