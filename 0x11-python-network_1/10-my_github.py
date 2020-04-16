#!/usr/bin/python3
if __name__ == "__main__":
    from requests import auth, get
    from sys import argv

    url = get('https://api.github.com/user',
              auth=auth.HTTPBasicAuth(argv[1], argv[2]))
    try:
        js = url.json()
        print(js.get("id"))
    except ValueError:
        print("None")
