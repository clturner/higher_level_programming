#!/usr/bin/python3
"""
takes Github credentials, uses the Github API to display your id
"""
import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    if r.text[12:27] == 'Bad credentials':
        print("None")
    else:
        print(r.json()['id'])
