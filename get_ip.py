import psutil
import platform

def ip() :
    if platform.system() == 'Linux' :
        return psutil.net_if_addrs()['enp0s1'][0].address
    elif platform.system() == 'Darwin' :
        return psutil.net_if_addrs()['en0'][1].address