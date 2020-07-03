#!/usr/bin/python3
"""
displays the value of the X-Request-Id variable found in header of respon\
se
"""
import urllib.request
import urllib.parse
import sys
import urllib.response
import urllib.error

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.URLError as e:
        ResponseData = e.read().decode("utf8", 'ignore')
        print('Error code: {}'.format(e.code))
