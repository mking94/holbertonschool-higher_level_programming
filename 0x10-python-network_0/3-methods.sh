#!/bin/bash
# Display allowed http method 
curl -sI -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
