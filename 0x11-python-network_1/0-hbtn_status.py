#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request

    url = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(response.read())))
        print("\t - content: {}".format(html))
        print("\t - utf8 content: {}".format(html.decode('utf-8')))
