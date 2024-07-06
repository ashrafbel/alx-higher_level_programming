#!/usr/bin/python3
"Script that takes a URL, sends a request to it, and displays the response body."
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        r = urllib.request.Request(url)
        with urllib.request.urlopen(r) as rs:
            body = rs.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
         print('Error code:', er.code)

