#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let va = '';
      for (let j = 0; j < this.width; j++) {
        va = va + 'X';
      }
      console.log(va);
    }
  }
};
