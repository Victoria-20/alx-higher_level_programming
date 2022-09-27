#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    text = res.text
    print("Body response:")
    print(f"\t- type: {type(text)}")
    print(f"\t- content: {text}")
