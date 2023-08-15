#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let va = '';
      for (let j = 0; j < this.width; j++) {
        va = va + c;
      }
      console.log(va);
    }
  }

  rotate () {
    let temp = 1;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
