#!/usr/bin/node
const argument = process.argv;
const size = parseInt(argument[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let i = 0; i < size; i++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
