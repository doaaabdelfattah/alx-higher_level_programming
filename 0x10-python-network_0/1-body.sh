#!/bin/bash
# cURL to the end
curl -s -w "%{http_code}" "$1"
