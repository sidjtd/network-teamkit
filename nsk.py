#!/usr/bin/env python

import subprocess
import argparse
import re
from modules import *
from modules.ipmapping import get_ip as getip
from modules.clientbrowser import view_site as viewhtml


## 2. IP Mapping - This tool will return the corresponding IP address of any domain entered.
def getipnow(domain_name):
    res = getip(domain_name)
    if (res == False):
        print('This Domain name does not exist')
    else:
        print('\nThe domain \"{}\"'.format(domain_name[0]), 'is associated with the following IP Address(es):')
        for each in res:
            print(' -', each[0])

## 4. Client Browser
def browsenow(site):
    res = viewhtml(site)

## Argument Parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Team Haxxor Kit', description ='Under Dev')
    subparsers = parser.add_subparsers(help='Module specific utilities')   

    # ii. ip mapping
    parser_getip = subparsers.add_parser('getip', help='DNS Related Help Functions')
    parser_getip.add_argument('hostname', nargs=1, help='Return ip address of host name, if it exists')
    parser_getip.set_defaults(func=getipnow)

    # iv. client browser
    client_browser = subparsers.add_parser('geturl', help='Quickly review any HTML')
    client_browser.add_argument('url', nargs=1, help='Return HTML page')
    client_browser.set_defaults(func=browsenow)


    args = parser.parse_args()
    print('Arguments: {}'.format(args))
    if('url' in args):
        browsenow(args.url)
    
    elif('hostname' in args):
        getipnow(args.hostname)
    