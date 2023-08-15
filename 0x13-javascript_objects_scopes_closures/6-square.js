#!/usr/bin/node
const SquareTop = require('./5-square');
module.exports = class Square extends SquareTop {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
