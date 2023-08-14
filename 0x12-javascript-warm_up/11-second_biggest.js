#!/usr/bin/node
let second = 0;
let first = 0;
if (process.argv.length > 3) {
  first = parseInt(process.argv[2]);
}
for (let i = 3; i < process.argv.length; i++) {
  if (process.argv[i] > first) {
    second = first;
    first = process.argv[i];
  }
}
console.log(second);
