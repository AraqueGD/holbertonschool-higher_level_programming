#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.error

    url = urllib.request.Request(argv[1])
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
