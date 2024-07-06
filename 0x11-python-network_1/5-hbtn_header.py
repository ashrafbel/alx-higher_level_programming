#!/usr/bin/python3
"A Python script: fetches URL, displays X-Request-Id from response header."
import requests
from sys import argv

if __name__ == '__main__':
    r_s = requests.get(argv[1])
    print(r_s.headers.get('X-Request-Id'))
