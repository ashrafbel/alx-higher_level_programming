#!/usr/bin/python3
"Accepts a URL, sends request, displays response body."
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r_s = requests.get(url)
    if r_s.status_code >= 400:
        print("Error code: {}".format(r_s.status_code))
    else:
        print(r_s.text)
