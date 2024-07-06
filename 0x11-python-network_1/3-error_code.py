#!/usr/bin/python3
"""
Script that takes a URL, sends a request to it, and displays the response body.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as rs:
            print(rs.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
