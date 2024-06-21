def guess_passwords():
    import random

    print('1-I can guess numbers 2- I can guess passwords')
    answer = input('enter the number of the option you want: ')
    
    if answer == '1':
        print('Enter the length of the number you want me to guess')
        answer1 = input('(for example (1) means from 0 to 9, and (2) means from 10 to 99): ')
        N_list = [str(random.randint(0,9)), str(random.randint(10,99)), str(random.randint(100,999)), str(random.randint(1000,9999)), str(random.randint(10000,99999)), str(random.randint(100000,999999)), str(random.randint(1000000,9999999)), str(random.randint(10000000,99999999)), str(random.randint(100000000,999999999)), str(random.randint(1000000000,9999999999))]
        Nu_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        if answer1 in Nu_list:
            index_Nu_list = Nu_list.index(answer1)
            print('the number is', N_list[index_Nu_list])
        else:
            print('I cant guess a number with this length'
                 )
    
    if answer == '2':
        t = 1
        password = input("enter your password (4 numbers): ")
        while True:
            GP1 = str(random.randint(1000,9999))
            if GP1 == password:
              print('password is:', GP1)
              print('number of attempts :', t )
              break
            else:
              t = t + 1
              print(GP1, '/////////wrong', t)
              pass