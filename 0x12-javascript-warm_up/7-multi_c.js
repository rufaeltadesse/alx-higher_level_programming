#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
