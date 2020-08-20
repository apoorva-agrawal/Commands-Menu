def my_menu():
    import subprocess as sp
    from termcolor import colored
    while True:
        print("****** Command Menu ******\n")
        print('Press 1: to open firefox browser')
        print('Press 2: to open notepad')
        print('Press 3: to display date')
        print('Press 4: to display calender')
        print('Press 5: exit\n\n')
        print('Enter your choice: ', end = '')
        param = input()
        print("result: ")

        if int(param) ==1:
            data = sp.getstatusoutput("firefox")
            print(data)
            print('\n')
            

        elif int(param) ==2:
            data = sp.getstatusoutput("notepad")
            print(data)
            print('\n')
             

        elif int(param) ==3:
            data = sp.getstatusoutput("date")
            print(data)
            print('\n')
             

        elif int(param) ==4:
            data = sp.getstatusoutput("cal")
            print(data)
            print('\n')
 
        else:
            break
        print(colored('SUCCESS\n','green'))if data[0]==0 else print(colored('FAILURE\n','red'))
    exited = print(colored('EXITED','blue'))
    return exited
  
