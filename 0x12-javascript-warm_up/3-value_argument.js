#!/usr/bin/node
const argument = process.argv;
if (argument.length === 2) {
  console.log('No argument');
} else {
  if (argument.length === 3) { console.log(argument[2]); }
}
