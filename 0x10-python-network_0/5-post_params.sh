#!/bin/bash
# sends POST reuest to the url and displays the body
curl -s -X "POST" "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
