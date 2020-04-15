#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        print("{}".format(response.info().get("X-Request-Id")))
