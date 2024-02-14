#!/usr/bin/node
const argument = process.argv;
if (typeof argument[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(argument[2]);
}
