from os import system
from sys import argv

def ping(ip):
    if system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1") == 0:
        return("UP !")
    else:
        return("DOWN !")
