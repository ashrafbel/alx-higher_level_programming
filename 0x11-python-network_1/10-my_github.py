#!/usr/bin/python3
"Uses Github API with credentials to display ID."
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    n = sys.argv[1]
    pss = sys.argv[2]
    tk = HTTPBasicAuth(n, pss)
    rt = requests.get('https://api.github.com/user', auth=tk)
    print(rt.json().get('id'))
