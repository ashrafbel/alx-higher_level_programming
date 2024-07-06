#!/usr/bin/python3
"sends POST request to http://0.0.0.0:5000/search_user with letter as param"
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    try:
        rs = requests.post(url, data=payload)
        js_data = rs.json()

        if js_data:
            print(f"[{js_data['id']}] {js_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
