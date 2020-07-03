#!/usr/bin/python3
"""
displays value of variable X-Request-Id in response header
"""
import requests
import sys

if __name__ == "__main__":
        r = requests.get(sys.argv[1])
        a = r.headers.get('X-Request-Id')
        print(a)
