def my_menu():
    import subprocess as sp
    from termcolor import colored
    history = []

    while True:
        print("****** Command Menu ******\n")
        print('Press 1: to open firefox browser')
        print('Press 2: to open notepad')
        print('Press 3: to display date')
        print('Press 4: to display calender')
        print('Press 5: to display history')
        print('Press 6: exit\n\n')
        print('Enter your choice: ', end = '')
        param = input()


        if int(param) <=6:

            if int(param) ==1:
                data = sp.getstatusoutput("firefox")
                history.append('firefox')

            elif int(param) ==2:
                data = sp.getstatusoutput("notepad")
                history.append('notepad')

            elif int(param) ==3:
                data = sp.getstatusoutput("date")
                history.append('date')

            elif int(param) ==4:
                data = sp.getstatusoutput("cal")
                history.append('cal')

            elif int(param) ==5:
                print(colored('HISTORY','blue'))
                print(colored(history,'blue'))
                history.append('history')

            else:
                break

            print('status:')
            if int(param) <=4:
                if data[0]==0:
                    print(colored('SUCCESS\n','green'))
                else:
                    print(colored('FAILURE\n','red'))

            print('result')
            print(data)
            print('\n')

        else:
            print(colored('INVALID COMMAND! Kindly enter right command \n','red'))
       
    exited = print(colored('EXITED','blue'))
    return exited
  
