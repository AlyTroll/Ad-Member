
from arsein.Arsein import Messenger
from os import system
from colorama import *
from random import choice
import random
import os
import rainbowtext,pyfiglet
os.system("clear")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
green = '\033[32m' 
red = '\033[31m' 
green = '\033[32m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'
from time import sleep
def printlow(Str):

    for char in Str:

        print(char, end='', flush=True)

        sleep(.01)
#اینجا هرچی اوث دارید بزارید
auths = input("هر مقدار اوث دارین رو وارد کنید : ")
os.system('clear')
print(rainbowtext.text(pyfiglet.figlet_format("Ali TROLL")))
printlow(red+"_"*60)
printlow (f"""
{yellow}└──>{red}Ali
{yellow}└───>>{red}TROLL
{yellow}└────>>>{red}God
""")
printlow(red+"_"*60)
num = 0
print("")
printlow(f"""
{yellow}1 به گروه 2 کانال با لینک 3 کانال با ایدی

‌[{red}1{yellow}]-join Group
[{red}2{yellow}]-join Channel
[{red}3{yellow}]-join channel ba id""")
print("")
out = input(red+'\noption : '+yw)
print('')
if out == '1':
		Link_Group = input("لینک گپ رو وارد کنید : ")
		os.system("clear")
		print(rainbowtext.text(pyfiglet.figlet_format("Ali TROLL")))
		print(pe+"ID Rubika : @Lockader_kronos")
		print(red+"_"*130)
		for auth in auths:
		    bot = Messenger(auth)
		    try:
		        Beni = bot.joinGroup(Link_Group)
		        num +=1
		        if Beni['status'] == "OK" :
		            print(green+"auth"+yw,num,green+"join")
		        else:
		                print(lrd+"not add"+yw,num,lrd+"auth") 
		                
		    except:pass
elif out == '2':
		            Link_Channel = input(red+'لینک چنل رو وارد کنید : '+yw)
		            os.system("clear")
		           
		            print(rainbowtext.text(pyfiglet.figlet_format("Ali TROLL")))
		            print(red+"ID Rubika :@lockader_kronos")
		            print(green+"_"*130)
		            for auth in auths:
		                bot = Messenger(auth)
		                try:
		                    Ben = bot.joinChannelByLink(Link_Channel)
		                    num +=1
		                    if Ben['status'] == "OK" :
		                        print(green+"auth"+yw,num,green+"join")
		                    else:
		                            print(lrd+"not add"+yw,num,lrd+"auth")
		            
		                except:pass
elif out == '3':
		                        Link_Channelbyid = input(red+'لینک چنل رو وارد کنید : '+yw)
		                        os.system("clear")
		                       
		                        print(rainbowtext.text(pyfiglet.figlet_format("Ali TROLL")))
		                        print(rd+"ID Rubika : @Lockader_kronos")
		                        print(green+"_"*130)
		                        for auth in auths:
		                            bot = Messenger(auth)
		                            try:
		                                baby = bot.joinChannelByID(Link_Channelbyid)
		                                num +=1
		                                if baby['status'] == "OK" :
		                                    print(green+"auth"+yw,num,green+"join")
		                                else:
		                                        print(lrd+"not add"+yw,num,lrd+"auth")
		                        
		                            except:pass
