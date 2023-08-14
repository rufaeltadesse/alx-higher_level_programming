#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let va;
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    va = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      va = va + 'X';
    }
    console.log(va);
  }
}
