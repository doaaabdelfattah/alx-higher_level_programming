#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
