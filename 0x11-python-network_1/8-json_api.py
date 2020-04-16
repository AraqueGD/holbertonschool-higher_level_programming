#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    try:
        response = requests.post(url, data)
        js = response.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except ValueError:
        print("Not a valid JSON")
