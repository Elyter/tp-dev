from socket import gethostbyname
from sys import argv

def lookup(ip) :
    return gethostbyname(ip)