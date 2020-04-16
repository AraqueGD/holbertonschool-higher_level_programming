#!/usr/bin/python3
if __name__ == "__main__":
    from requests import get, auth
    from sys import argv

    repo = argv[1]
    user = argv[2]
    url = get(
        'https://api.github.com/repos/{}/{}/commits'.format(repo, user))
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
        print("Not valid JSON")
