#!/bin/bash
# Script that display http response code
curl -s -o -w '%{http_code}' "$1"
