#!/usr/bin/python3
""" takes in URL and an email, sends POST request to the URL
    with email as a parameter, display body of response
    use packages urllib and sys
"""

if __name__ == "__main__":
    import requests
    import sys

    email = {"email": sys.argv[2]}

    res = requests.post(sys.argv[1], data=email)
    print(res.text)
