#!/usr/bin/python

import requests
import sys

MONIT_URL = sys.argv[1]     #Monit _status url e.g. http://localhost:2812/_status
MONIT_USER = sys.argv[2]    #Monit user
MONIT_PASS = sys.argv[3]    #Monit pass


i = 0
r = requests.get(MONIT_URL, auth=(MONIT_USER, MONIT_PASS), stream=True)
res = ''
res += '{ "data":[ '
res += "\n"
for line in r.iter_lines():
    if 'Process ' in line:
        if i == 0:
            res += '   { "{#MONIT_PROCESS}":"' + line.split()[1].replace('\'', '') + '"}'
            i = 1
        else:
            res += '   ,{ "{#MONIT_PROCESS}":"' + line.split()[1].replace('\'', '') + '"}'
        res += "\n"




res += ' ] }'

print res
            
