import socket
import re

# This module method uses socket to get the IP Addresses associated
# with a domain string

results = []
def get_ip(domain_name):
    name = domain_name[0]
    if(re.match('http://', name)):
        name = name[7:]
    elif(re.match('https://', name)):
        name = name[8:]
    res = socket.getaddrinfo(name, 80)
    for each in res:
        if(len(each)<6 and len(each)>4):
            results.append(each[4])
    return set(results)