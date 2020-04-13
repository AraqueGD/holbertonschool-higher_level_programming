#!/bin/bash
# Status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
