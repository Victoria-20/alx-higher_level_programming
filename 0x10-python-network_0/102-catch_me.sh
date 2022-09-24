#!/bin/bash
# takes in the url as argument, send GET request and display body
curl -sH "X-School-User-Id: 98" "$1"
