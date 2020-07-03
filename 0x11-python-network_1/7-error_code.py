#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":

    e = requests.get(sys.argv[1])
    if e.status_code <= 400:
        print(e.text)
    else:
        print('Error code: {}'.format(e.status_code))
