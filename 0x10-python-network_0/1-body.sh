#!/bin/bash
# takes in the url, send GET request, display response body
curl -sfL "$1" -X GET
