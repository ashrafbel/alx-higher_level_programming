#!/usr/bin/python3
"""
This script accepts a URL, sends a request to it
and displays the value of the 'X-Request-Id'
variable found in the response headers.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as rs:
        hs = rs.headers
        x_id_r = hs.get("X-Request-Id")
        print(x_id_r)
