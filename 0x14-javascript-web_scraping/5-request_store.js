#!/usr/bin/node

const fs = require('fs');
const request = require('request');
// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];
// Create a writable stream for the file
const writeStream = fs.createWriteStream(filePath, 'utf8');

// Make a GET request to the specified URL
request.get(url)
    .on('error', (err) => {
        console.error('Error fetching webpage:', err);
    })
    .pipe(writeStream)
    .on('finish', () => {
        console.log('File saved successfully:', filePath);
    });
