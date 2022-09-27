#!/usr/bin/python3
""" sends request to url and displays value of X-Request-Id
    variable found in the header of the response
    use packages urllib and sys
"""

if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    header = res.headers.get("X-Request-Id")
    print(header)
