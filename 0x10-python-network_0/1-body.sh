#!/bin/bash
# Send get request and display the statut code 
curl -s -o /dev/Null -w "%{http_code}" "$1"
