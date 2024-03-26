#!/usr/bin/node
const request = require('request');

// Make a Get request to URL
const url = process.argv[2];
request.get(url, (error, responce) => {
  if (error) {
    console.error('Error', error);
  } else {
    console.log('code:', responce.statusCode);
  }
});
