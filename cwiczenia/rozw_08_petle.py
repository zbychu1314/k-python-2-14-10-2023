import random

X_SIZE = 100
Y_SIZE = 100

def calculate(x_secret,y_secret,x_user,y_user):
    x_result = abs(x_secret-x_user)
    y_result = abs(y_secret-y_user)
    return x_result, y_result

def losuj_skarb():
    x_secret = random.randint(0,X_SIZE)
    y_secret = random.randint(0,X_SIZE)
    return x_secret,y_secret

def cieplo_zimno():
    list_results =[[]]
    x_secret,y_secret = losuj_skarb()
    x_user = random.randint(0,X_SIZE)
    y_user = random.randint(0,X_SIZE)
    #kroki =0
    #while kroki < liczba_krokow:
    #liczba_krokow =2*min(x_secret,y_secret,x_user,y_user)
    #print(f'liczba_krokow {liczba_krokow}')
    print(f'Pozycja skarbu {x_secret},{y_secret}')
    found_treasure = False
    x_result_init, y_result_init = calculate(x_secret,y_secret,x_user,y_user)
    list_results.append([x_result_init,y_result_init])
    if x_result_init ==0 and y_result_init ==0:
        print(f'You WIN')
        found_treasure =True
    while found_treasure == False:
        print(f'Twoja pozycja {x_user},{y_user}')
        direction = input('Podaj kierunek(w,a,s,d): ')
        if 'w' in direction:
            y_user+=1
            if y_user >Y_SIZE:
                print('Pozycja poza zakresem koniec gry')
                return -1
            x_result, y_result = calculate(x_secret,y_secret,x_user,y_user)
            list_results.append([x_result,y_result])
            if list_results[-2][1]<list_results[-1][1]:
                print('Zimno')
            else:
                print('Cieplo')
        elif 's' in direction:
            y_user-=1
            if y_user <0:
                print('Pozycja poza zakresem koniec gry')
                return -1
            x_result, y_result = calculate(x_secret,y_secret,x_user,y_user)
            list_results.append([x_result,y_result])
            if list_results[-2][1]<list_results[-1][1]:
                print('Zimno')
            else:
                print('Cieplo')
        elif 'd' in direction:
            x_user+=1
            if x_user >X_SIZE:
                print('Pozycja poza zakresem koniec gry')
                return -1
            x_result, y_result = calculate(x_secret,y_secret,x_user,y_user)
            list_results.append([x_result,y_result])
            if list_results[-2][0]<list_results[-1][0]:
                print('Zimno')
            else:
                print('Cieplo')
        elif 'a' in direction:
            x_user-=1
            if x_user <0:
                print('Pozycja poza zakresem koniec gry')
                return -1
            x_result, y_result = calculate(x_secret,y_secret,x_user,y_user)
            list_results.append([x_result,y_result])
            if list_results[-2][0]<list_results[-1][0]:
                print('Zimno')
            else:
                print('Cieplo')
        if list_results[-1][0]==x_secret and list_results[-1][1]==y_secret:
            print(f'You WIN')
            found_treasure =True
cieplo_zimno()   
        
            
        

