#!/usr/bin/python3
""" sends request to url and displays value of X-Request-Id
    variable found in the header of the response
    use packages urllib and sys
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
