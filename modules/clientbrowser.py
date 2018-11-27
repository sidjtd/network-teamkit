import re
import socket
from urllib.request import urlopen

# This tool will return the corresponding 
# IP address of any domain entered.


# Because urlopen requires a full URL, this function will account for URL arguments entered without 'http://' or
# 'http://www.' and prepend them to the arguments as needed

results = []
def view_site(arg):
    url = arg[0]
    if(re.match(r'www', url)):
        url = re.sub(r'www.', 'http://www.', url)
        print('haga', url)
    else:
        url = 'http://www.{}'.format(url)
    if(re.match(r'http://www', url)):
        res = urlopen(url)
        for each in res:
            print(each)