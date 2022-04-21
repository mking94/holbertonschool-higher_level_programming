#!/bin/bash
# Script that display http response code
curl -s -w -X GET '%{http_code}\n' "$1"
