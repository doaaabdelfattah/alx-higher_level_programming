#!/usr/bin/node

const fs = require('fs');
const request = require('request');
// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return;
        }
        console.log('File saved successfully:', filePath);
    });
});
