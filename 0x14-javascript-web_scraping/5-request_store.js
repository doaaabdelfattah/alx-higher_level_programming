#!/usr/bin/node

const fs = require('fs');
const request = require('request');
// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
