#!/usr/bin/node
const argument = process.argv;
const number = parseInt(argument[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else { console.log('My number: ' + number); }
