#!/usr/bin/node
const { argv } = require('node:process');
let second = 0;
let first = 0;
let flagCount = 0;
if (argv.length > 3)
first = parseInt(argv[2]);
for (let i = 3; i < argv.length; i++) {
  if (argv[i] > first) {
    second = first;
    first = argv[i];
  }
}
console.log(second);

