#!/usr/bin/python3
"this script for fetches status url"
import requests


if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    rs = requests.get(url)
    txt = rs.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
