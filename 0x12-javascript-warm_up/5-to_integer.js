#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parseInt(argv[2]));
}
