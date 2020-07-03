#!/usr/bin/python3
"""
displays the value of the X-Request-Id variable found in header of response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        the_page = response.read()
        print(the_page.decode('utf8'))
