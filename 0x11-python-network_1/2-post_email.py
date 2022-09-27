#!/usr/bin/python3
""" takes in URL and an email, sends POST request to the URL
    with email as a parameter, display body of response
    use packages urllib and sys
"""

if __name__ == "__main__":
    import urllib
    from urllib.request import urlopen
    import sys

    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    with urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
