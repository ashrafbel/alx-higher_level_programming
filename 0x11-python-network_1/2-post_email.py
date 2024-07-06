#!/usr/bin/python3
"""
A script that takes a URL and an email, sends a POST request
and displays the response body.
"""

import urllib.parse
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    e = sys.argv[2]
    u = 'utf-8'

    val = urllib.parse.urlencode({'email': e}).encode(u)
    re = urllib.request.Request(url, data=val, method='POST')
    with urllib.request.urlopen(re) as rs:
        r_body = rs.read().decode(u)
    print(r_body)
