#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse

    url = argv[1]
    email = argv[2]
    value = {'email': email}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        email_post = response.read()
        print(email_post.decode('utf-8'))
