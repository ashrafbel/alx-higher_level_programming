#!/usr/bin/python3
"A script: takes URL, email, sends POST request, displays response body."
import requests
from sys import argv

if __name__ == '__main__':
    p = {'email': argv[2]}
    rs = requests.post(argv[1], data=p)
    print(rs.text)
