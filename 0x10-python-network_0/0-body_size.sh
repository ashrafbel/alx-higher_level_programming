#!/bin/bash
# This bash script for sends a request to a URL and displays the size of the response body in bytes
curl -sI $1 | grep -i Content-Length
