#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv

    url = requests.get(argv[1])
    print(url.headers.get('X-Request-Id'))
