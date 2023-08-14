#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let va;
  for (let i = 0; i < parseInt(argv[2]); i++) {
    va = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      va = va + 'X';
    }
    console.log(va);
  }
}
