#!/bin/bash
# sends reuest to url as argument and display status code of the response
curl -s -w "%{http_code}" "$1" -o /dev/null
