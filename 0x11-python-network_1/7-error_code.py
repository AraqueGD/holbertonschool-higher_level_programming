#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv

    url = requests.get(argv[1])
    error_code = url.status_code
    if (error_code >= 400):
        print("Error Code: {}".format(error_code))
    else:
        print(url.text)
