from os import system
from sys import argv

print(system("ping -c 5 " + argv[1]))