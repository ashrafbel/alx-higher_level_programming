#!/usr/bin/python3
"""this script for fetches https://alx-intranet.hbtn.io/status"""
import requests
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    rs = r.text
    print("Body response:")
    print("\t- type: {}".format(type(rs)))
    print("\t- content: {}".format(rs))
