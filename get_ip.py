import psutil

def ip() :
    return psutil.net_if_addrs()['en0'][0].address