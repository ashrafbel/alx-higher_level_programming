#!/bin/bash
# this script for show supported HTTP methods for a URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
