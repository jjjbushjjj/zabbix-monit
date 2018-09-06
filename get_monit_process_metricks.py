#!/usr/bin/python

import requests
import sys
import lxml.html as lh

MONIT_URL = sys.argv[1]         # Monit _status usr e.g. http://localhost:2812/_status
MONIT_USER = sys.argv[2]        # Monit user
MONIT_PASS = sys.argv[3]        # Monit pass
MONIT_PROCESS = sys.argv[4]     # Monit process name (from discovery)
MONIT_METRICK = sys.argv[5]     # Monit metrick name (left column in table)

tmp = MONIT_URL.split('/')
MONIT_URL = tmp[0] + '//' + tmp[2] + '/' + MONIT_PROCESS

page = requests.get(MONIT_URL, auth=(MONIT_USER, MONIT_PASS))

doc = lh.fromstring(page.content)
tr_elements_col1 = doc.xpath('//tr/td[position()=1]')
tr_elements_col2 = doc.xpath('//tr/td[position()=2]')

for idx, t in enumerate(tr_elements_col1):
    if t.text_content() == MONIT_METRICK:
        print tr_elements_col2[idx].text_content()
