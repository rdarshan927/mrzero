import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 rd927tor.py')
    run('mkdir /usr/share/aut')
    run('cp rd927tor.py /usr/share/aut/mrzerotor.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/mrzerotor.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/mrzerotor.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now Tor Ip changer  has been removed successfully')
