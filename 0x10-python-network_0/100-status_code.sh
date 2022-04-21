#!/bin/bash
# Script that display http response code
curl -s -o  /dev/null -w '%{http_code}' "$1"
