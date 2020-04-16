#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, auth
    from sys import argv

    url = get(
        'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2]))
    # repo #user
    try:
        js = url.json()
        for ten in js[:10]:
            sha = ten.get('sha')
            commit = ten.get('commit')
            if (commit):
                author = commit.get('author')

            if (author):
                name = author.get('name')
            print("{}: {}".format(sha, name))
    except ValueError:
        print("No valid JSON")
