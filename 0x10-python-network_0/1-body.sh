#!/usr/bin/bash
# Send get request and display the statut code 
curl -s -o /dev/null -w "%{http_code}" "$1"
