#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const argument = process.argv;
const NumOne = parseInt(argument[2]);
const NumTwo = parseInt(argument[3]);

console.log(add(NumOne, NumTwo));
