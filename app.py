import os
import platform

OS_type = platform.system()
OS_type = OS_type.lower()


def shutdown(time):
    '''
    It automate shutdown by scheduling the 
    time for computer to shutdown
    '''

    if OS_type == 'linux':
        shutdown_str = 'shutdown -t '+ str(time)
    elif OS_type == 'windows':
        shutdown_str == 'shutdown -s -t ' + str(time)
    else:
        print('Sorry this feature is not available in ', OS_type)
        return

    os.system(shutdown_str)

def cancel_shutdown():
    if OS_type == 'linux':
        cancel_str = 'shutdown -c'
    elif OS_type == 'windows':
        cancel_str = 'shutdown -a'
    else:
        return
    os.system(cancel_str)

def main():
    print('Use Shutup To schedule your shutdown'.center(50, '='))
    print('1.Automate Shutdown\n2.Cancel shutdown')
    option = int(input('Option here: '))
    if option == 1:
        time = int(input('\nEnter time to shutdown in seconds : '))
        shutdown(time)
    elif option == 2:
        cancel_shutdown()
        print('Shutdown successful canceled ...')
    else:
        print('Invalid option try again!!!\n')
        main()


if __name__ == '__main__':
    main()