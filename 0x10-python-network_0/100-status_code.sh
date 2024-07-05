#!/bin/bash
# Script to send a request to a URL and display only the response status code
curl -o /dev/null -s -w "%{http_code}" "$1"
