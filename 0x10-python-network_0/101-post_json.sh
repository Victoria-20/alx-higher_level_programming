#!/bin/bash
# sends a JSON reuest to the url as argument and display body of response
curl -s -X POST $1 -H 'Content-Type: application/json' -d @$2
