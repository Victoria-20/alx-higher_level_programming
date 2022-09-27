#!/usr/bin/python3
""" takes in URL, sends request to the URL
    display body of response
    use packages urllib and sys
"""

if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
