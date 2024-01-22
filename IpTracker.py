# Just try to find out the logic :v
# I didn't have time to make a comment
import platform
platform = platform.system()

version ='1.2.15'

title = '''
██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Ip tracker | Ip tracker script | Ip tracker python | Tracker
Author  : MrKriszz 
Github  : https://github.com/MrKriszz
'''
import os
import sys
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=False)
import requests
import json
import time
import os

sys.stdout.write("\x1b]2;IpTracker By MrKriszz\x07")

if os.name == 'posix':
	c = os.system('which pip')
	if c == 256:
		os.system('sudo apt-get install python-pip')
	else:
		pass
else:
	print ('Kriszz: Check your pip installer')
try:
	import requests,colorama
except:
	try:
		if os.name == 'posix':
			os.system('sudo pip install colorama')
			sys.exit('Kriszz: I have installed necessary modules for you')
		elif os.name == 'nt':
			os.system('pip install colorama')
			sys.exit('Kriszz: I have installed nessecary modules for you')
		else:
			sys.exit('Kriszz: Download and install necessary modules')
	except Exception as e:
		print ('Kriszz: ',e)
if os.name == 'nt':
	colorama.init()
time.sleep(1)
os.system('cls||clear')
print('''IpTracker By MrKriszz [Version '''+version+'''] - Platform '''+platform+'''   ''')
print(Fore.LIGHTRED_EX + title)

def main():

    print(Fore.LIGHTBLUE_EX)
    ipaddress = input("Ip Address/Domain: ")
    print(Fore.LIGHTYELLOW_EX)
    print('Address: '+ipaddress)
    print(Fore.LIGHTGREEN_EX)
    iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")
	
    if iprequest.status_code == 200:

		
        ipdata = json.loads(iprequest.text)

        if ipdata["status"] == "success":
            print('-'.center(100,'-'))
            lat = ipdata["lat"]
            lon = ipdata["lon"]
            maps = f"{lat},{lon}"
            print('|Country     : ', ipdata["country"], ipdata["countryCode"])
            print('|Region      : ', ipdata["regionName"], ipdata["region"])
            print('|City        : ', ipdata["city"])
            print('|Zip         : ', ipdata["zip"])
            print('|Location    : ', lat , "," ,lon)
            print('|Timezone    : ', ipdata["timezone"])
            print('|ISP         : ', ipdata["isp"])
            print('|Ip Address  : ', ipdata["query"])
            print('|Map         : ', maps )
            print('-'.center(100,'-'))
            main()
        else:
            print(Fore.RED + "ERROR:"+Fore.LIGHTRED_EX+" Address/Domain '"+Fore.LIGHTYELLOW_EX + ipaddress +Fore.LIGHTRED_EX+'''' not found!''' + Fore.LIGHTBLUE_EX+''' 
INFO:'''+Fore.LIGHTRED_EX+''' Try Address/Domain 'google.com, microsoft.com or 8.8.8.8.' ''')
            main()
main()
