#!/usr/bin/node

const fs = require('fs');
const request = require('request');
// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  // Check if the request was successful (status code 200)
  if (response.statusCode === 200) {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        return;
      }
      console.log('File saved successfully:', filePath);
    });
  } else {
    console.error('Failed to fetch webpage. Status code:', response.statusCode);
  }
});
