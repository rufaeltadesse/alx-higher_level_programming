#!/usr/bin/node
function factorial (a) {
  if (a >= 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
const { argv } = require('node:process');
console.log(factorial(parseInt(argv[2])));
