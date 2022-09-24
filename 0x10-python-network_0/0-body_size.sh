#!/bin/bash
# takes in the url,sends request to url,display size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
