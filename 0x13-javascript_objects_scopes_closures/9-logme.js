#!/usr/bin/node
let countVal = 0;
exports.logMe = function count (item) {
  console.log(`${countVal}: ${item}`);
  countVal += 1;
};
