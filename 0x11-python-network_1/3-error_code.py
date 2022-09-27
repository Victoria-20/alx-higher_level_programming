#!/usr/bin/python3
""" takes in URL, sends request to the URL
    display body of response
    use packages urllib and sys
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code:", err.code)
