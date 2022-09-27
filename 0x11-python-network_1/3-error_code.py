#!/usr/bin/python3
""" takes in URL, sends request to the URL
    display body of response
    use packages urllib and sys
"""

if __name__ == "__main__":
    from urllib.request import urlopen, error
    import sys

    try:
        with urlopen(sys.argv[1], data) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code:", err.code)
