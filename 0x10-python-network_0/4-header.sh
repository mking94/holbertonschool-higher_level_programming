#!/bin/bash
# Send header, http method and recive the url content
curl -H "X-School-User-Id: 98" -X GET "$1"
