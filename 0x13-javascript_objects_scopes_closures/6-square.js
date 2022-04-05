#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const line = new Array(Number(this.size)).fill((c || "X"));
    for (let i = 0; i < this.size; i++) {
      console.log(line.join(''));
    }
  }
};
