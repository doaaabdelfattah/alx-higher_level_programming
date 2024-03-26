#!/usr/bin/node

const request = require('request');

// Get the URL from the command-line arguments
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    // Parse the JSON response body
    console.log(data.title);
  }
});
