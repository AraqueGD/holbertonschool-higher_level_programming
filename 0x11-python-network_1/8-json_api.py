#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) > 1):
        dic = {'q': argv[1]}
    else:
        dic = {'q': ""}
    try:
        url = requests.post(url, dic)
        js = url.json()

        if (not js):
            print("Not result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except ValueError:
        print("Not a valid JSON")
