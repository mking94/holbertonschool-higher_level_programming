#!/bin/bash
# Send variables with post method using curl
curl -s -X POST --data {"email":"test@gmail.com","subject":"I will always be here for PLD"} "$1"
