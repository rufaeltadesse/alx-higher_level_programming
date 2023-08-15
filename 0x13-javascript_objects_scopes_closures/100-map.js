#!/usr/bin/node
const my = require('./100-data').list;

console.log(my);
console.log(my.map((x, idx) => x * idx));
