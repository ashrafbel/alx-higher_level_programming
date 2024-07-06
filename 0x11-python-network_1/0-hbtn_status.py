#!/usr/bin/python3
# this script for fetches URL

import urllib.request
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as rs:
    ct = rs.read()
    print("Body response:")
    print(f"\t- type: {type(ct)}")
    print(f"\t- content: {ct}")
    print(f"\t- content: {ct}")
    print(f"\t- utf8 content: {ct.decode('utf-8')}")
