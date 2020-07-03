#!/usr/bin/python3
# displays the value of the X-Request-Id variable found in header of response
import urllib.request
import sys
import urllib.response

if __name__ == "__main__":

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        a = response.getheader('X-Request-Id')
        print(a)
