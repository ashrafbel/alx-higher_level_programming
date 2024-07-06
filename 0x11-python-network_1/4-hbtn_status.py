#!/usr/bin/python3
"this script for fetches status url"
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    rs = requests.get(url)
    
    if rs.status_code == 200:
        print("- body:")
        print("\t- type:", type(rs.text))
        print("\t- content:", rs.text)
