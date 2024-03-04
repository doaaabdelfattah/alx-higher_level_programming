#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request to the URL
curl -sI "$1"
