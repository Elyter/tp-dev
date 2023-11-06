from lookup import lookup
from is_up import ping
from get_ip import ip
from sys import argv

if argv[1] == "lookup":
    result = lookup(argv[2])
elif argv[1] == "ping":
    result = ping(argv[2])
elif argv[1] == "ip":
    result = ip()

print(result)
