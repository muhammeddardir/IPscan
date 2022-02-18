#!/usr/bin/env python 

import optparse
import os
import argparse
import subprocess
from termcolor import *
from colored import fg, bg, attr 



'''---------------------------------Banner-------------------------------------'''
print(" ")
print(colored("______                      _   _        ", "red", attrs=['bold']))
print(colored("|  _  \                    | | (_)       ", "red", attrs=['bold']))
print(colored("| | | |   __ _   _ __    __| |  _   _ __ ", "red", attrs=['bold']))
print(colored("| | | |  / _` | | '__|  / _` | | | | '__|", "red", attrs=['bold']))
print(colored("| |/ /  | (_| | | |    | (_| | | | | |   ", "red", attrs=['bold']))
print(colored("|___/    \__,_| |_|     \__,_| |_| |_|   ", "red", attrs=['bold']))
print(" ")
print ('%s 		Coded By @muhammed_dardir v1  %s' % (fg(40), attr(1)))
print(colored("", "white", attrs=['bold']))



'''---------------------------------Init-------------------------------------'''

parser = argparse.ArgumentParser(description='This Framework to do IP Enum and Scanning')
parser.add_argument("-t","--target", help="-t domain")
args = parser.parse_args()
target=args.target
subprocess.call("mkdir " + target, shell=True)
'''---------------------------------Tools-------------------------------------'''
# metabigor
print(colored("[+] Get CIDR", 'blue', attrs=['bold']))
subprocess.call("echo " +target+" | metabigor net --org  >>" +target+"/CIDR.txt", shell=True)

# mapcidr
print(colored("[+] From CIDR Get IPs", 'blue', attrs=['bold']))
subprocess.call("mapcidr -l "+target+"/CIDR.txt -silent >"+target+"/IPss.txt", shell=True)
subprocess.call("cat "+target+"/IPss.txt|sort|uniq >"+target+"/IPs.txt", shell=True)
subprocess.call("rm "+target+"/IPss.txt", shell=True)

# nrich
print(colored("[+] Scanning Open Ports in each IP and Find a related vulnerabilities", 'blue', attrs=['bold']))
subprocess.call("nrich -o json "+target+"/IPs.txt >"+target+"/IP_nrich.json", shell=True)

# httpx
print(colored("[+] Check a Live Host", 'blue', attrs=['bold']))
subprocess.call("cat "+target+"/IPs.txt|httpx -silent -t 100000 >"+target+"/Live_IPs.txt", shell=True)





