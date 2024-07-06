#!/usr/bin/python3
"""
This script accepts a URL, sends a request to it
and displays the value of the 'X-Request-Id'
variable found in the response headers.
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as rs:
    hs = rs.headers
    x_id_r = hs.get("X-Request-Id")
print(x_id_r)
