#!/usr/bin/node

const request = require('request');

// Get the URL from the command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON response body
    const data = JSON.parse(body);

    // Initialize a counter for the number of movies with Wedge Antilles
    let count = 0;

    // Loop through each film
    data.results.forEach(film => {
      // Check if Wedge Antilles is present in the list of characters for the film
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });

    // Print the count of movies where Wedge Antilles is present
    console.log(count);
  }
});
